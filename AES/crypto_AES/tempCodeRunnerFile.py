from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
FLAG = "crypto{p3n6u1n5_h473_3cb}"
plaintext = input()
plaintext = bytes.fromhex(plaintext)
padded = pad(plaintext + FLAG.encode(), 16)

print(padded)