### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
###Make a program that asks for a note, between zero and ten. Show a message if the value is invalid and keep asking until the user enters a valid value.

while True:
    try:
        nota= int(input(' Digite um valor de 0 a 10 : '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    else:
        if 0<=nota<=10:
            print(f'A nota informada é: {nota}')
            break
        else:
            print('O número deve estar entre 0 e 10')
