lista = []
lista.append(123)
lista.append(234)
lista.append(345)
lista.append("ABC")
lista.append("BCD")
lista.append("CDE")
lista.append(True)
# lista.append(False)
# lista.remove(False)

# print(lista)
pituus = len(lista)
# print(pituus)

for alkio in lista[3:6]:
    print(alkio)


##### tuple-tyyppi #####

monikko = (123, "ABC", True)
monikko[0] = 234
print(monikko)
