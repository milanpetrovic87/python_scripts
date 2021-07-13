#!/usr/bin/python3

lista = [3,6,9,1]
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print (lista)
