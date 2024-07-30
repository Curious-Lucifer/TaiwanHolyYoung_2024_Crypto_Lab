import requests
from Crypto.Util.number import long_to_bytes


def factordb(n: int):
    factordb_api_url = 'http://factordb.com/api'
    resp = requests.get(factordb_api_url, params = { 'query': n })
    resp.raise_for_status()

    factors = [[int(factor)] * power for factor, power in resp.json()['factors']]
    factors = sum(factors, [])
    return factors


n = 13910994564373802167
e = 65537
c = 1407190981767527409

p, q = factordb(n)
phin = (p - 1) * (q - 1)
d = pow(e, -1, phin)
m = pow(c, d, n)

print(long_to_bytes(m))
