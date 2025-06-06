#!/usr/bin/env python3

import os

from utils import CTFd


### ==================================== ###

SERVER='127.0.0.1'
CTFD='http://localhost'
USERNAME='admin'
PASSWORD='password'

### ==================================== ###


client = CTFd(CTFD, USERNAME, PASSWORD)
for root, _, files in os.walk('.'):
    if 'task.yml' in files:
        chal_id = client.create_challenge(os.path.join(root, 'task.yml'), SERVER)
