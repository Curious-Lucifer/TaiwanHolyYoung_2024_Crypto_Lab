from Crypto.Util.number import long_to_bytes, bytes_to_long

p, q = 3538692379, 3931111573
e = 65537
c = 1407190981767527409

d = pow(e, -1, (p - 1) * (q - 1))

print(long_to_bytes(pow(c, d, p * q)))
