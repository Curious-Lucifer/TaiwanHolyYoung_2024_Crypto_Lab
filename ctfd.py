#!/usr/bin/env python

import os

import secret

from ctfdtools.client import CTFdClient


client = CTFdClient(secret.CTFD, username=secret.USERNAME, password=secret.PASSWORD)
for root, _, files in os.walk('.'):
    if 'task.yml' in files:
        challenge = client.init_challenge(root, server=secret.SERVER)
        challenge.create()
