# Faça um programa que leia 5 números e informe a soma e a média dos números.
i=0
lista= []
for i in range(5):
    numero = float(input('Digite um número:'))
    lista.append(numero)
    somaemedia=sum(lista)/len(lista)
print(f"A soma dos números é {sum(lista)}")
print(f'A média dos 5 números é:{somaemedia}')
