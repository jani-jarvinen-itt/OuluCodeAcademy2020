import random
ARVAUSKERTOJEN_MAKSIMI_MAARA = 3

oikealuku = random.randint(1,20)
# print(oikealuku)
arvauskertojen_maara = 0

while (arvauskertojen_maara < ARVAUSKERTOJEN_MAKSIMI_MAARA):
    print("Arvaa luku välillä 1-20:")
    arvaus = int(input())
    # print(arvaus)

    if (arvaus < oikealuku):
        print("Oikea luku on suurempi.")
    elif (arvaus > oikealuku):
        print("Oikea luku on pienempi.")
    else:
        print("Arvasit oikein!")
        break

    arvauskertojen_maara = arvauskertojen_maara+1

print("Peli on päättynyt.")
