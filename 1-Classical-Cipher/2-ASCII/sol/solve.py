payload = '46 4c 41 47 7b 4a 75 73 74 5f 61 5f 73 69 6d 70 6c 65 5f 50 79 74 68 6f 6e 5f 73 63 72 69 70 74 21 7d'
flag = ''.join(chr(int(code, 16)) for code in payload.split())
print(flag)