# Faça um programa para imprimir:
#   1
#  2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
numero = int(input("Digite um numero"))
lista = [numero]
listafinal = []
lista2 = lista * numero
maximo = len(lista2)
r = 1
for x in lista2:
    listafinal = [r] * r

    print(listafinal)
    r = r + 1
