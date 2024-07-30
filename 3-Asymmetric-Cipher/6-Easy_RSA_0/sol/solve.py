import requests
from Crypto.Util.number import long_to_bytes


def factordb(n: int):
    factordb_api_url = 'http://factordb.com/api'
    resp = requests.get(factordb_api_url, params = { 'query': n })
    resp.raise_for_status()

    factors = [[int(factor)] * power for factor, power in resp.json()['factors']]
    factors = sum(factors, [])
    return factors


n = 2639362258825246588480470347939064671401603842072135672799
e = 65537
c = 1746618984754679181914163060955061486968283106432500087220

p, q, r = factordb(n)
phin = (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phin)
m = pow(c, d, n)

print(long_to_bytes(m))
