from random import randint

tent = 0
chute = 0
Num = randint(1, 100)

while chute != Num:
    chute = int (input("chute?  "))
    tent = tent + 1
    if chute > Num:
        print("chutou alto porra!")
    elif chute < Num:
        print("chutou baixo! mocinha")
print("tentativas :", tent)