##Make a Program that reads three numbers and shows the biggest one.
##Faça um Programa que leia três números e mostre o maior deles.
n1=float(input("Digite o valor do primeiro numero : "))
n2=float(input("Digite o valor do segundo numero: "))
n3=float(input("Digite o valor do terceiro numero: "))

if n1>n2 and n1>n3:
    print(" o valor do maior numero é :" +str(n1))
if n2>n1 and n2> n3:
    print(" o valor do maior numero é :" + str(n2))
if n3>n1 and n3>n2 :
    print(" o valor do maior numero é :" + str(n3))
if n1==n2==n3 :
    print("Os três números são iguais")