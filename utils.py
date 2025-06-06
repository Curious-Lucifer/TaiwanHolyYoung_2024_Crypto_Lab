import re
import sys
import os
import enum
import tempfile
import logging
import contextlib
import zipfile
from typing import Annotated
from urllib import parse as url_parse

import requests
import bs4
import yaml
from pydantic import BaseModel, StringConstraints, EmailStr


logger = logging.getLogger('ctftools-logger')
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(stdout_handler)


@contextlib.contextmanager
def change_path(path: str):
    origin_path = os.getcwd()
    try:
        os.chdir(os.path.normpath(path))
        yield
    finally:
        os.chdir(origin_path)


def compress2zip(path_list: list[str], zip_path: str):
    zipdir_path = os.path.basename(zip_path).removesuffix('.zip')
    def archive_path(path: str):
        path_parts = os.path.normpath(path).split(os.sep)
        path_parts[0] = zipdir_path
        return os.path.join(*path_parts)

    archive_files = {}
    for path in path_list:
        if os.path.isfile(path):
            archive_files[archive_path(path)] = path
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    archive_files[archive_path(file_path)] = file_path

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as f:
        for apath, path in archive_files.items():
            f.write(path, apath)


def url_join(url: str, path: str):
    if not url.endswith('/'):
        url += '/'
    if path.startswith('/'):
        path = path[1:]
    return url_parse.urljoin(url, path)


def info(msg: str):
    logger.info(f'[\033[34m*\033[0m] {msg}')


def success(msg: str):
    logger.info(f'[\033[32m+\033[0m] {msg}')


def warning(msg: str):
    logger.warning(f'[\033[33m#\033[0m] {msg}')


def error(msg: str):
    logger.error(f'[\033[31m!\033[0m] {msg}')


class ChallengeType(str, enum.Enum):
    STANDARD = 'standard'
    DYNAMIC = 'dynamic'


class ChallengeState(str, enum.Enum):
    HIDDEN = 'hidden'
    VISIBLE = 'visible'


class DynamicValueFunction(str, enum.Enum):
    LOGARITHMIC = 'logarithmic'
    LINEAR = 'linear'


class DynamicValue(BaseModel):
    function: DynamicValueFunction
    initial: int
    minimum: int


class ChallengeBase(BaseModel):
    name: str
    category: str
    description: str | None = None
    author: str | None = None
    connection_info: str | None = None

    type: ChallengeType
    value: int | DynamicValue
    state: ChallengeState


class Challenge(ChallengeBase):
    flag: str | None = None
    tags: list[str] | None = None
    distfiles: list[str] | None = None
    files: list[str] | None = None
    hints: list[str] | None = None

    canonical_name: Annotated[
        str, StringConstraints(pattern=r'^[a-z0-9-]+$')] | None = None


class ChallengeCreate(ChallengeBase):
    pass


class CTFd:
    def __init__(self, url: str, username_email: str, password: str):
        self._url = url
        self._session = requests.session()
        self._csrf_token = None

        self._login(username_email, password)

    def _login(self, username_email: str, password: str):
        res = self._session.get(url_join(self._url, '/login'))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        nonce = soup.find(id='nonce').attrs.get('value')

        info(f'Try to login CTFd as "{username_email}"')
        res = self._session.post(url_join(self._url, '/login'), data={
            'name': username_email, 'password': password, 'nonce': nonce,
            '_submit': 'Submit'
        })
        res.raise_for_status()

        self._set_context()
        success('Login success')

    def _set_context(self):
        res = self._session.get(self._url)
        res.raise_for_status()
        m = re.search(r'\'csrfNonce\'\s*:\s*"([0-9a-f]+)"', res.text)
        token = m.group(1)
        self._session.headers['Csrf-Token'] = token
        self._csrf_token = token

    def get_api_url(self, api_path: str):
        base = url_join(self._url, '/api/v1/')
        return url_join(base, api_path)

    def create_challenge_basic(self, chal: ChallengeCreate) -> int:
        chal_data = chal.model_dump(exclude_none=True)
        if 'author' in chal_data:
            author = chal_data.pop('author')
            if 'description' in chal_data:
                chal_data['description'] = chal_data['description'].rstrip() + '\n\n<br>\n\n'
            else:
                chal_data['description'] = ''
            chal_data['description'] += f'Author : {author}'
    
        if chal_data['type'] == 'dynamic':
            value = chal_data.pop('value')
            chal_data.update(value)

        info(f'. Creating challenge "{chal_data['name']}"')
        res = self._session.post(self.get_api_url('/challenges'), json=chal_data)
        res.raise_for_status()
        return res.json()['data']['id']

    def add_challenge_flag(self, chal_id: int, flag: str):
        info('. Add flag to challenge')
        res = self._session.post(
            self.get_api_url('/flags'),
            json={'content': flag, 'data': '', 'type': 'static',
                  'challenge': chal_id})
        res.raise_for_status()

    def add_challenge_tag(self, chal_id: int, tag: str):
        info(f'... Add tag "{tag}" to challenge')
        res = self._session.post(
            self.get_api_url('/tags'), json={'value': tag, 'challenge': chal_id})
        res.raise_for_status()

    def add_challenge_hint(self, chal_id: int, hint: str):
        info('... Add hint to challenge')
        res = self._session.post(
            self.get_api_url('/hints'),
            json={
                'challenge_id': chal_id,
                'content': hint, 'cost': 0, 'requirements': {'prerequisites': []}
            })
        res.raise_for_status()

    def add_challenge_file(self, chal_id: int, file_path: str):
        with open(file_path, 'rb') as f:
            info(f'... Add file "{os.path.basename(file_path)}" to challenge')
            res = self._session.post(
                self.get_api_url('/files'),
                data={
                    'nonce': self._csrf_token, 'type': 'challenge',
                    'challenge': chal_id
                },
                files={'file': f})
            res.raise_for_status()

    def create_challenge(self, path: str, server: str = '<SERVER>'):
        info('Creating challenge')
        with open(path) as f:
            y = yaml.safe_load(f.read())
        challenge = Challenge(**y)

        if challenge.connection_info is not None:
            challenge.connection_info = challenge.connection_info.format(server=server)

        chal_id = self.create_challenge_basic(
            ChallengeCreate.model_validate(challenge.model_dump()))
        if challenge.flag is not None:
            self.add_challenge_flag(chal_id, challenge.flag)
        if challenge.tags is not None:
            info('. Add tags to challenge')
            for tag in challenge.tags:
                self.add_challenge_tag(chal_id, tag)
        if challenge.hints is not None:
            info('. Add hints to challenge')
            for hint in challenge.hints:
                self.add_challenge_hint(chal_id, hint)
        if (challenge.files is not None):
            info('. Add files to challenge')
            with change_path(os.path.dirname(path)):
                for file in challenge.files:
                    self.add_challenge_file(chal_id, file)
        if (challenge.distfiles is not None) and (challenge.canonical_name is not None):
            info('. Pack and add files to challenge')
            with change_path(os.path.dirname(path)):
                with tempfile.TemporaryDirectory() as temp_path:
                    zip_path = os.path.join(temp_path, f'{challenge.canonical_name}.zip')
                    compress2zip(challenge.distfiles, zip_path)
                    self.add_challenge_file(chal_id, zip_path)
        success('Success create challenge')
        return chal_id
