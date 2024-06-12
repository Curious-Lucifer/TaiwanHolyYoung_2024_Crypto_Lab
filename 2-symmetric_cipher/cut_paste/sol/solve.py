import requests as req

session = req.session()

# username=Curious
# 0000000000000000
# ssssss&money=100
# ................
session.post('http://34.80.39.230:12000/login', data = {'username': 'Curious0000000000000000ssssss'})

token = bytes.fromhex(session.cookies.get('token'))
new_token = token[:16] + token[32:48] + token[16:32] + token[48:]
session.cookies.set('token', None)
session.cookies.set('token', new_token.hex())

response = session.get('http://34.80.39.230:12000/get-flag')
print(response.content)