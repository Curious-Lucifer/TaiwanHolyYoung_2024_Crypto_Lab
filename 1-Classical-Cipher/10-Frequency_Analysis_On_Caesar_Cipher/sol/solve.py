import string
import hashlib


def caesar_decrypt(cipher: str, offset: int):
    offset = offset % 26
    cipher = cipher.upper()
    return ''.join(string.ascii_uppercase[(string.ascii_uppercase.index(char) - offset) % 26] for char in cipher)


def simple_freq_analysis(message: str) -> int:
    message = list(message.lower())
    english_freq = [
        8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
        0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
        2.758, 0.978, 2.360, 0.150,  1.974, 0.074
    ]
    message_freq = [100 * message.count(s) / len(message)
                    for s in string.ascii_lowercase]
    return int(sum(((mf - ef) / ef) ** 2
                   for mf, ef in zip(message_freq, english_freq)))


with open('cipher.txt') as f:
    cipher = f.read()


approx_list = []
for offset in range(26):
    approx_list.append(simple_freq_analysis(caesar_decrypt(cipher, offset)))
plain = caesar_decrypt(cipher, approx_list.index(min(approx_list)))


print(plain)
print(f'FLAG{{{hashlib.sha256(plain.encode()).hexdigest()}}}')
