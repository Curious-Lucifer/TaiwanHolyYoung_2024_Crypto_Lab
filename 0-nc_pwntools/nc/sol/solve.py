from pwn import *

from CTFLib.Utils import *


r = nc('nc 34.80.39.230 10000')
r.recvlines(2)

r.recvline()
r.sendlineafter(b'> ', b'Curious')

r.recvline()
r.sendlineafter(b'> ', b'is')

r.recvline()
r.sendlineafter(b'> ', b'so')

r.recvline()
r.sendlineafter(b'> ', b'handsome')

r.recvline()
r.sendlineafter(b'> ', b'!')

r.interactive()