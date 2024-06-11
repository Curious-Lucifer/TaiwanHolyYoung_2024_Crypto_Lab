#!/usr/bin/env python3

import os

from dotenv import load_dotenv

from CTFdTools.challenge import Challenge
from CTFdTools.ctfd import CTFd


load_dotenv('.env.dev')
ctfd = CTFd(os.getenv('BASE_URL'), os.getenv('API_KEY'))

challenges_path = []
for root, _, files in os.walk('.'):
    if 'task.yml' in files:
        challenges_path.append(root)

challenges = [
    Challenge(challenge_path, os.getenv('CHALLENGE_SERVER'), ctfd)
    for challenge_path in challenges_path
]

for challenge in challenges:
    challenge.load_yaml()
    challenge.create()
