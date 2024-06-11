import sys
import os

from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, long_to_bytes

from secret import FLAG


def pad(message: bytes):
    pad = 16 - (len(message) % 16)
    return message + bytes([pad]) * pad


def unpad(message: bytes):
    pad = message[-1]
    assert 0 < pad <= 16
    assert message.endswith(bytes([pad]) * pad)
    return message[:-pad]


def generate_RSA_key():
    p, q = getPrime(1024), getPrime(1024)
    n, e = p * q, 0x10001
    d = pow(e, -1, (p - 1) * (q - 1))
    return (n, e), (n, d)


def RSA_decrypt(c, RSA_privkey):
    return pow(c, RSA_privkey[1], RSA_privkey[0])


def exchange_AES_key(RSA_pubkey, RSA_privkey):
    print(f'Setup RSA Public Key > {RSA_pubkey}')

    print(f'Setup > Give me AES Key encrypt by RSA Public Key')
    try:
        c = int(input('> '))
    except ValueError:
        print('Error : not integer')
        sys.exit()
    AES_key = long_to_bytes(RSA_decrypt(c, RSA_privkey), 16)

    print(f'Setup > Give me AES IV encrypt by RSA Public Key')
    try:
        c = int(input('> '))
    except ValueError:
        print('Error : not integer')
        sys.exit()
    AES_iv = long_to_bytes(RSA_decrypt(c, RSA_privkey), 16)

    return AES_iv, AES_key


def encrypt(iv: bytes, key: bytes, plain: bytes):
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    return aes.encrypt(pad(plain))


def decrypt(iv: bytes, key: bytes, cipher: bytes):
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    try:
        return unpad(aes.decrypt(cipher))
    except AssertionError:
        print('Error : padding incorrect')
        sys.exit()


def challenge(iv: bytes, key: bytes):
    nonce = os.urandom(0x1000)

    print(f'Check > {encrypt(iv, key, nonce).hex()}')
    try:
        cipher = bytes.fromhex(input('> '))
    except ValueError:
        print('Error : not hex string')
        sys.exit()

    if decrypt(iv, key, cipher) != (key + nonce):
        print('Erorr : challenge failed')
        sys.exit()

    print(f'Check > {encrypt(iv, key, iv + nonce).hex()}')


def main():
    print('Description : Communicate With CuriousGPT In A Secure Way')

    RSA_pubkey, RSA_privkey = generate_RSA_key()
    AES_iv, AES_key = exchange_AES_key(RSA_pubkey, RSA_privkey)

    challenge(AES_iv, AES_key)

    print(f'CuriousGPT > {encrypt(AES_iv, AES_key, FLAG).hex()}')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()