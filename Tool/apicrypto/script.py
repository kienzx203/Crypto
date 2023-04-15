from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
key = bytes.fromhex("0424974c68530290458c8d58674e2637f65abc127057957d7b3acbd24c208f93")#sha256
iv = bytes.fromhex("01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10")
cipher = bytes.fromhex("E5 60 44 09 42 C4 BB DE F6 A1 2D 93 D9 1D 13 72 AF 8D 4C F7 A7 9F 1F B9 99 68 9C B8 C2 4C 4F 85")
dd = AES.new(key, AES.MODE_CBC, iv)
print(unpad(dd.decrypt(cipher),16))

