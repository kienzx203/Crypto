from urllib.request import urlopen
from itertools import cycle
import json

url = 'https://aes.cryptohack.org/bean_counter/'
png_header_hex = '89504e470d0a1a0a0000000d49484452'
png_header = bytes.fromhex(png_header_hex)


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


response = json.loads(urlopen(url + 'encrypt/').read())
ciphertext = bytes.fromhex(response['encrypted'])
key = xor(ciphertext, png_header)
plaintext = xor(ciphertext, cycle(key))

open('bean_flag.png', 'wb').write(plaintext)
