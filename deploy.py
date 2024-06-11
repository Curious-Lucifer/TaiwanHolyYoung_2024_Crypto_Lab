#!/usr/bin/env python3

import os
import subprocess
import sys
import yaml

if len(sys.argv) != 2:
    print('Usage : ./deploy.py {start/stop}')
    sys.exit()


challenges_path = []
for root, _, files in os.walk('.'):
    if 'task.yml' in files:
        challenges_path.append(root)

for challenge_path in challenges_path:
    with open(os.path.join(challenge_path, 'task.yml')) as f:
        data = yaml.safe_load(f)
    if 'compose' not in data:
        continue

    compose_path = data['compose']
    canonical_name = data['canonical_name']

    if sys.argv[1] == 'start':
        command = f'COMPOSE_PROJECT_NAME={canonical_name} docker compose -f {compose_path} up -d'
        success_message = f'[\033[92m+\033[0m] Build {data["category"]}:{data["name"]} Success'
        error_message = f'[\033[91mX\033[0m] !!! Build {data["category"]}:{data["name"]} Error !!!'
    elif sys.argv[1] == 'stop':
        command = f'COMPOSE_PROJECT_NAME={canonical_name} docker compose -f {compose_path} stop'
        success_message = f'[\033[92m+\033[0m] Stop {data["category"]}:{data["name"]} Success'
        error_message = f'[\033[91mX\033[0m] !!! Stop {data["category"]}:{data["name"]} Error !!!'
    else:
        print('Error : Unrecognized Command')
        sys.exit()

    try:
        subprocess.run(command, 
            shell = True, 
            check = True, 
            cwd = challenge_path, 
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE
        )
        print(success_message)
    except subprocess.CalledProcessError:
        print(error_message)


