from Crypto.Cipher import AES


key = bytes.fromhex('77e9ed71d1d4ea27816aa0538c091f14')
cipher = bytes.fromhex('75924759583675f4a56c2c322c72be86')

aes = AES.new(key, AES.MODE_ECB)
plain = aes.decrypt(cipher)

print(plain)
