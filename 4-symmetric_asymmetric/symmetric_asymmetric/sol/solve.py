import os

from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from pwn import *

from CTFLib.Utils import *


def pad(message: bytes):
    pad = 16 - (len(message) % 16)
    return message + bytes([pad]) * pad


def unpad(message: bytes):
    pad = message[-1]
    assert 0 < pad <= 16
    assert message.endswith(bytes([pad]) * pad)
    return message[:-pad]


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


r = nc('nc 34.80.39.230 14000')
r.recvline()

n, e = eval(r.recvline().strip().split(b'> ')[1])

# Exchange AES Key & AES IV
iv = os.urandom(16)
key = os.urandom(16)

c = pow(bytes_to_long(key), e, n)
r.recvline()
r.sendlineafter(b'> ', str(c).encode())

c = pow(bytes_to_long(iv), e, n)
r.recvline()
r.sendlineafter(b'> ', str(c).encode())


# Challenge
cipher = bytes.fromhex(r.recvline().strip().split(b'> ')[1].decode())
nonce = decrypt(iv, key, cipher)

r.sendlineafter(b'> ', encrypt(iv, key, key + nonce).hex().encode())

cipher = bytes.fromhex(r.recvline().strip().split(b'> ')[1].decode())
assert decrypt(iv, key, cipher) == iv + nonce


# Get Flag
cipher = bytes.fromhex(r.recvline().strip().split(b'> ')[1].decode())
print(decrypt(iv, key, cipher))


r.close()