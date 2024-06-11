import sys
import os

from Crypto.Cipher import AES

from secret import FLAG


MAX_ATTEMPS = 10000

def pad(message: bytes):
    return message + b'\0' * (16 - (len(message) % 16))

def encrypt(plain: bytes, key: bytes):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(pad(plain))

def main():
    print('Description : Input Prefix & Get Cipher Of (Prefix + Flag)')
    assert len(FLAG) <= 16

    key = os.urandom(32)

    for _ in range(MAX_ATTEMPS):
        try:
            prefix = bytes.fromhex(input('> '))
        except ValueError:
            print('Error : not hex string')
            sys.exit()

        cipher = encrypt(prefix + FLAG, key)
        print(f'Oracle > {cipher.hex()}')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
