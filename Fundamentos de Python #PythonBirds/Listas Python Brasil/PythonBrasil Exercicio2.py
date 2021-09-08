#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

i=0
lista= []
lista2=[]
for i in range(10):
    numero = int(input('Digite um número:'))
    lista.append(numero)

print(lista)
lista.reverse()

print( lista)
