from Crypto.Util.number import getPrime, bytes_to_long, isPrime

from secret import FLAG

base = getPrime(1024) + 1

p = base + getPrime(32)
while not isPrime(p):
    p = base + getPrime(32)

q = base + getPrime(32)
while not isPrime(q):
    q = base + getPrime(32)

n = p * q
e = 65537

c = pow(bytes_to_long(FLAG), e, n)

print(f'{n, e = }')
print(f'{c = }')