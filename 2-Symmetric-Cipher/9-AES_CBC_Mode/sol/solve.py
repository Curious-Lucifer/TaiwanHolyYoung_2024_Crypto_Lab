from Crypto.Cipher import AES


key = bytes.fromhex('d1e138810051ac8deaef9fd33c969e080003d3f87d264dd431190f0e7795528b')
iv = bytes.fromhex('25741419227aece3cb4f715f1c2b3878')
cipher = bytes.fromhex('af6ab08a9380c038328bec3c47e70b915bbf4faf0e4b72db5f56d274bd6be5458552b6023e64f10a492bb88e839e51516b50903363bc637a1fe2550317392564')

aes = AES.new(key, AES.MODE_CBC, iv=iv)
plain = aes.decrypt(cipher)

print(plain)
