# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# Make a program that asks for the price of three products and inform you which product you should buy, knowing that the decision is always for the cheapest.
produto1 = str(input("Digite o nome do primeiro produto: "))
n1 = float(input("Digite o valor do primeiro produto: "))
produto2 = str(input("Digite o nome do segundo produto: "))
n2 = float(input("Digite o valor do segundo produto: "))
produto3 = str(input("Digite o nome do terceiro produto: "))
n3 = float(input("Digite o valor do terceiro produto: "))

if n1 < n2 and n1 < n3:
    print(" o valor do menor preço  é :" + str(n1))
    print(" E o produto é :" + str(produto1))
if n2 < n1 and n2 < n3:
    print(" o valor do menor numero é :" + str(n2))
    print(" E o produto é :" + str(produto2))
if n3 < n1 and n3 < n2:
    print(" o valor do menor numero é :" + str(n3))
    print(" E o produto é :" + str(produto3))