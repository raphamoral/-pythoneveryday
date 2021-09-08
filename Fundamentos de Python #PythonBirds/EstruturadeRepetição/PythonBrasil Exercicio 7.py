#7.Faça um programa que leia 5 números e informe o maior número.
numerob=[]

while True:
    try:
        numeroa=int(input((" Digite um número : ")))
        numerob.append(numeroa)
        numeroa=int(input((" Digite um número : ")))
        numerob.append(numeroa)

        numeroa=int(input((" Digite um número : ")))
        numerob.append(numeroa)
        numeroa=int(input((" Digite um número : ")))
        numerob.append(numeroa)
        numeroa=int(input((" Digite um número : ")))
        numerob.append(numeroa)
        print(numerob)
        print(max(numerob))
        break
    except ValueError:
        print('Deve ser fornecido um valor inteiro')