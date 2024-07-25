"""Cut & Paste 的小工具."""

import os
from urllib import parse as url_parse

from Crypto.Cipher import AES


KEY = os.urandom(32)


def pad(message: bytes) -> bytes:
    """把輸入的 message 加上一直加上 \0 直到長度是 16 的倍數
    
    Args:
        message: 要填充的位元組
    Returns
        回傳填充好 \0 的位元組，這個位元組的長度一定是 16 的倍數
    """

    return message + b'\0' * (16 - (len(message) % 16))


def unpad(message: bytes) -> bytes:
    """把輸入的 message 去掉填充的 \0.
    
    Args:
        message: 已經被 \0 填充過的位元組
    Returs:
        回傳去掉填充的位元組
    """

    return message.rstrip(b'\0')


def encrypt(plain: bytes) -> bytes:
    """用 AES ECB Mode 加密輸入的 plain.
    
    Args:
        plain: 要加密的位元組
    Returns
        回傳已經被加密過的位元組，並且 plain 在加密前已經填充過 \0 到長度是 16 的倍數
    """

    aes = AES.new(KEY, AES.MODE_ECB)
    return aes.encrypt(pad(plain))


def decrypt(cipher: bytes) -> bytes:
    """用 AES ECB Mode 解密輸入的 cipher.
    
    Args:
        cipher: 要解密的位元組
    Returns:
        回傳已經被解密過的位元組，並且這個位元組已經去掉填充的 \0 了
    """

    aes = AES.new(KEY, AES.MODE_ECB)
    return unpad(aes.decrypt(cipher))


def is_username_valid(username: str) -> bool:
    """確認使用者名稱是否符合規則（不能有 = 和 & 在使用者名稱內）.
    
    Args:
        username: 要確認是否符合規則的使用者名稱
    Returns:
        輸入的使用者名稱是否符合規定沒有 = 和 & 這兩個符號
    """

    return not (('=' in username) or ('&' in username))


def userdata2token(userdata: dict[str, str | int]) -> str:
    """把使用者相關資料轉換成代表使用者身份的 token.
    
    Args:
        userdata: 使用者的相關資料
    Returns:
        回傳代表使用者身份的 token
    """

    token = url_parse.urlencode(userdata)
    return encrypt(token.encode()).hex()


def token2userdata(token: str) -> dict[str, str | int]:
    """把代表使用者身份的 token 轉換成使用者相關資料.
    
    Args:
        token: 代表使用者身份的 token
    Returns:
        回傳使用者相關資料
    Raises:
        ValueError: token 格式有問題
    """

    try:
        token = decrypt(bytes.fromhex(token)).decode()
    except UnicodeDecodeError as e:
        raise ValueError('Invalid token') from e

    userdata = dict(url_parse.parse_qsl(token))
    if userdata.get('money') is None:
        raise ValueError('Invalid token') from e
    userdata['money'] = int(userdata['money'])
    return userdata
