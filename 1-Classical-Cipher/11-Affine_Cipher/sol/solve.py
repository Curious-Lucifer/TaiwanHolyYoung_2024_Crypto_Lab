import hashlib
from string import ascii_lowercase
from tqdm import trange


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'
cipher = open('cipher.txt').read()


def char2num(char: str):
    return alphabet.index(char)


def num2char(num: int):
    return alphabet[num]


def decrypt(cipher: str, a: int, b: int):
    a_inv = pow(a, -1, len(alphabet))
    plain = [(a_inv * (char2num(char) - b)) % len(alphabet) for char in cipher]
    return ''.join(num2char(num) for num in plain)


def simple_freq_analysis(message: str) -> int:
    message = list(message.lower())
    english_freq = [
        8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
        0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
        2.758, 0.978, 2.360, 0.150,  1.974, 0.074
    ]
    message_freq = [100 * message.count(s) / len(message)
                    for s in ascii_lowercase]
    return int(sum(((mf - ef) / ef) ** 2
                   for mf, ef in zip(message_freq, english_freq)))


approx_list = []
key_list = []
for a in trange(1, len(alphabet), leave=False):
    for b in range(len(alphabet)):
        plain_t = decrypt(cipher, a, b)
        approx_list.append(simple_freq_analysis(plain_t))
        key_list.append((a, b))

a, b = key_list[approx_list.index(min(approx_list))]
plain = decrypt(cipher, a, b)
print(plain)
print(f'FLAG{{{hashlib.sha256(plain.encode()).hexdigest()}}}')