from pwn import *

from CTFLib.Utils import *
from CTFLib.Crypto import *


r = nc('nc 34.80.39.230 12001')
r.recvline()

def oracle(prefix: bytes):
    r.sendlineafter(b'> ', prefix.hex().encode())
    return bytes.fromhex(r.recvline().strip().split(b'> ')[1].decode())

mgr = PrependOracleManager(oracle)
flag = mgr.attack()

print(flag)

r.close()