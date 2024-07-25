#!/usr/bin/env python3

import argparse
import os
import subprocess
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'stop'])

    args = parser.parse_args()

    challenge_paths = []
    for root, _, files in os.walk('.'):
        if 'task.yml' in files:
            challenge_paths.append(root)

    for challenge_path in challenge_paths:
        with open(os.path.join(challenge_path, 'task.yml')) as f:
            data = yaml.safe_load(f)

        if 'compose' not in data:
            continue

        compose_path = data['compose']
        canonical_name = data['canonical_name']

        if args.action == 'start':
            command = f'COMPOSE_PROJECT_NAME={canonical_name} docker compose -f {compose_path} up -d'
            success_message = f'[\033[92m+\033[0m] Build \'{data["category"]}\':\'{data["name"]}\' Success'
            error_message = f'[\033[91mX\033[0m] !!! Build \'{data["category"]}\':\'{data["name"]}\' Error !!!'
        elif args.action == 'stop':
            command = f'COMPOSE_PROJECT_NAME={canonical_name} docker compose -f {compose_path} down'
            success_message = f'[\033[92m+\033[0m] Stop \'{data["category"]}\':\'{data["name"]}\' Success'
            error_message = f'[\033[91mX\033[0m] !!! Stop \'{data["category"]}\':\'{data["name"]}\' Error !!!'

        try:
            subprocess.run(command, shell = True, check = True,
                cwd = challenge_path,
                stdout = subprocess.PIPE, stderr = subprocess.PIPE
            )
            print(success_message)
        except subprocess.CalledProcessError:
            print(error_message)


if __name__ == '__main__':
    main()
