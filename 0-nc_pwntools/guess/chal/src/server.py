import random
import sys

from secret import FLAG


def main():
    print('Description : Guess The Secret Number', end='\n\n')

    secret_num = random.randint(0, 255)
    for _ in range(256):
        try:
            inp_num = int(input('> '))
        except ValueError:
            print('Error : not integer')
            sys.exit()

        if inp_num > secret_num:
            print('CuriousGPT > Too big')
        elif inp_num < secret_num:
            print('CuriousGPT > Too small')
        else:
            print(f'Flag : {FLAG}')
            sys.exit()


if __name__ == '__main__':
    main()