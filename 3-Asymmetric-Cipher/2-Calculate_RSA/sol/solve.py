from Crypto.Util.number import long_to_bytes

p = 9835210563207632773
q = 10100395802203591453
e = 65537
c = 38901730400489769669866798139902101966


n = p * q
phin = (p - 1) * (q - 1)
d = pow(e, -1, phin)
m = pow(c, d, n)

print(long_to_bytes(m))
