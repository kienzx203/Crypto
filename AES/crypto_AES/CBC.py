import json
import requests
import os

URL_encrypt = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
URL_decrypt = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext}/"


def get_ciphertext():
    r = requests.get(URL_encrypt)
    json_ans = json.loads(r.text)
    return json_ans['ciphertext']


def get_plaintext(ciphertext):
    r = requests.get(URL_decrypt.format(ciphertext=ciphertext))
    json_ans = json.loads(r.text)
    return json_ans['plaintext']


def xor(itx, ity):
    return [x ^ y for x, y in zip(itx, ity)]


ciphertext = get_ciphertext()
# [0] is the IV, [1] and subsequent are the encryptions of the plaintext blocks.
split_ciphertext = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]

plaintext = [0]*(len(split_ciphertext) - 1)
for i in range(len(plaintext)):
    pi = bytes.fromhex(get_plaintext(split_ciphertext[i+1]))
    ci = bytes.fromhex(split_ciphertext[i])
    plaintext[i] = ''.join(map(chr, xor(pi, ci)))

print(f"Flag: {''.join(plaintext)}")

a = os.urandom(16)
print(a.hex())
b = os.urandom(16)
print(b.hex())
print(a.hex()+b.hex())
