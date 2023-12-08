
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_ardonata_ascendent = sorted(lista)
print(lista_ardonata_ascendent)


lista_ordonata_descendent = sorted(lista, reverse=True)
print(lista_ordonata_descendent)

#Slicere
indici_pari = lista[0::2]
print(indici_pari)

indici_impari = lista[1::2]
print(indici_impari)

#Multiplu de 3
def multiplu():
    for i in range(len(lista)):
        if (i % 3 == 0):
            print(i)

multiplu()