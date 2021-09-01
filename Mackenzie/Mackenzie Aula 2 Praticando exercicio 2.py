#Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo.
while True:
    try:
        numero1 = float(input(""))
        numero2 = float(input(""))
        break
    except ValueError:
        print('Deve ser fornecido um valor inteiro')

diferenca=(numero1-numero2)**2
print(diferenca)
