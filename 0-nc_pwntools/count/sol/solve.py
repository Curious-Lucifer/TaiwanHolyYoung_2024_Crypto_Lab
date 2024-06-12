from pwn import *

from CTFLib.Utils import *


r = nc('nc 34.80.39.230 10001')
r.recvlines(2)

for i in trange(100):
    r.sendlineafter(b'> ', str(i + 1).encode())

r.interactive()