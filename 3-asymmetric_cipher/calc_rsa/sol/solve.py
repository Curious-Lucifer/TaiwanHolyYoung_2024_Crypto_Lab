from Crypto.Util.number import long_to_bytes, bytes_to_long


p, q = 9835210563207632773, 10100395802203591453
e = 65537
c = 38901730400489769669866798139902101966

d = pow(e, -1, (p - 1) * (q - 1))

print(long_to_bytes(pow(c, d, p * q)))

