import random


def mix(string):
    alg_list = list(string)
    random.shuffle(alg_list)
    return ''.join(alg_list)


fnum1 = random.randint(0, 9)
fnum2 = random.randint(0, 9)
uLetter1 = chr(random.randint(65, 90))
uLetter2 = chr(random.randint(65, 90))
lLetter1 = chr(random.randint(97, 122))
lLetter2 = chr(random.randint(97, 122))
spcchar1 = chr(random.randint(33, 64))
spcchar2 = chr(random.randint(33, 64))

final_password = uLetter1 + uLetter2 + str(fnum1) + str(fnum2) + lLetter1 + lLetter2 + spcchar1 + spcchar2
final_password = mix(final_password)

print(final_password)
