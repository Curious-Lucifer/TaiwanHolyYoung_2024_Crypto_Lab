import requests as req

BASE_URL = 'http://34.81.172.164:10000'
s = req.session()

s.post(BASE_URL + '/login', data={'username': 'Curious0000000000000000ssssss'})

token = bytes.fromhex(s.cookies['token'])
token = token[:16] + token[32:48] + token[16:32] + token[48:]
s.cookies.set('token', None)
s.cookies.set('token', token.hex())

res = s.get(BASE_URL + '/get-flag')
print(res.json())
