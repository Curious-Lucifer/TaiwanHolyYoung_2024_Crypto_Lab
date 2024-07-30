from Crypto.Cipher import AES


key = bytes.fromhex('85f1c9f80a5b9e440380cf9b02b31ff46de4f864cd7c2ba32f7ec2881b07d71c')
cipher = bytes.fromhex('6b2f26db534ee26ab1c987cea73a2fecd1a3f8335c50412ffa785d3ce5b90ad310a064dfa4bf824bc7968d876c9e5d6917e1157fc27a29c2e042a82f08ed6c96')

aes = AES.new(key, AES.MODE_ECB)
plain = aes.decrypt(cipher)

print(plain)
