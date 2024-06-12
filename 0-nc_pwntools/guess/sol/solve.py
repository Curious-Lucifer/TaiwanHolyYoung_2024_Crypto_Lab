from pwn import *

from CTFLib.Utils import *


r = nc('nc 34.80.39.230 10002')
r.recvlines(2)

scope = [0, 256]
while True:
    print(scope)
    num = sum(scope) // 2
    r.sendlineafter(b'> ', str(num).encode())

    result = r.recvline()
    if b'big' in result:
        scope[1] = num
    elif b'small' in result:
        scope[0] = num + 1
    else:
        print(result)
        break

r.close()
