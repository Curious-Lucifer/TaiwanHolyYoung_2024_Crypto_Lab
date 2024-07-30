import string
import hashlib


def caesar_decrypt(cipher: str, offset: int):
    offset = offset % 26
    cipher = cipher.upper()
    return ''.join(string.ascii_uppercase[(string.ascii_uppercase.index(char) - offset) % 26] for char in cipher)


with open('cipher.txt') as f:
    cipher = f.read()


for i in range(26):
    print(caesar_decrypt(cipher, i))


# 可以找到有一段 cipher 特別符合英文單字的感覺
plain = 'THECAESARCIPHERISAREALLYOLDCIPHERWHICHISREALLYWEAKIMNOTSUREHOWOLDBECAUSEIMTOOLAZYTOLOOKATTHEWIKIPAGEATTHEMOMENTBUTIFIGUREITSGOTTOBEATLEASTLIKEFIFTYYEARSOLDORWHATEVERVAJDUXFCPVUSETHOSELASTTENCHARACTERSASTHESOLUTION'
print(f'FLAG{{{hashlib.sha256(plain.encode()).hexdigest()}}}')
