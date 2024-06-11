#!/usr/bin/env python3

import os

from CTFdTools.ctfd import CTFd
from CTFdTools.challenge import Challenge


ctfd = CTFd('.env.dev')

challenges: list[Challenge] = []
for root, _, files in os.walk('.'):
    if 'task.yml' in files:
        challenges.append(Challenge(root, ctfd))

for challenge in challenges:
    challenge.post()
