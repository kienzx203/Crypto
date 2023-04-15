# from random import randint

from Crypto.Util.number import long_to_bytes
a = 288260533169915
p = 1007621497415251

# FLAG = b'crypto{????????????????????}'


# def encrypt_flag(flag):
#     ciphertext = []
#     plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
#     for b in plaintext:
#         e = randint(1, p)
#         n = pow(a, e, p)
#         print(b)
#         if b == '1':
#             ciphertext.append(n)
#         else:
#             n = -n % p
#             ciphertext.append(n)
#     return ciphertext


# =====================Decode=======================
from Crypto.Util.number import long_to_bytes

a = 288260533169915
p = 1007621497415251

with open("output.txt", "r") as f:
    v = eval(f.read())

res = ""
for x in v:
    c = pow(x, (p-1)//2, p)
    if c == 1:
        res += "1"
    else:
        res += "0"

print(long_to_bytes(int(res, 2)))