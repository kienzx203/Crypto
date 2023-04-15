import gmpy2

n= 149583170767368182982427483589104137735568476029847987626896496007273106379122831875974487650387052772762031227903738171407276031738713136691531865195738064439168338782154929043076522460473952207414064710638997032356105723836504978088332238417145750716222412779224439377051124355942987463657471909922388297053
e= 65537

c= 1292388824308250413889931565779670794681429363528473914956124924973851952746553591901513127456003320

for i in range(10000):
    m, is_true_root = gmpy2.iroot(i*n + c, e)
    if is_true_root:
        print(f"Found i = {i}")
        print("Message: {}".format(bytearray.fromhex(format(m, 'x')).decode()))
        break