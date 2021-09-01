
#EXERCÍCIO 1 – Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação.
while True:
    try:
        numero1 = int(input(""))
        numero2 = int(input(""))
        break
    except ValueError:
        print('Deve ser fornecido um valor inteiro')



soma= numero1+numero2
divisao=numero1/numero2
subtracao= numero1-numero2
multiplicacao=numero1*numero2

divisaotruncada=numero1//numero2
resto=numero1%numero2
exponenciacao=numero1**numero2

print(soma )
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisaotruncada)
print(resto)
print(exponenciacao)


