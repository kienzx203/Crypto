from Crypto.Cipher import AES
import hashlib
from Crypto.Util.number import *
import tqdm
import random
import binascii
import requests


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted


result = requests.get(
    "https://aes.cryptohack.org/passwords_as_keys/encrypt_flag")
cipher = result.json()["ciphertext"]

with open('D://web//web//thuchanh//web_exploit//Crypto//AES//crypto_AES//word.txt', 'r') as f:
    for word in f:
        word = word.strip()
        KEY_1 = hashlib.md5(word.encode()).hexdigest()
        m = decrypt(cipher, KEY_1)
        if b'crypto{' in m:
            print(m)
            break
