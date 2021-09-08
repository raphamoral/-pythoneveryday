#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

numero=0
listas =[]
while True:
    try:
        numero= float(input(' Digite um valor de 0 a 10 : '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    if numero!=-1:
        listas.append(numero)
    else:
        break
print(len(listas))#a
print(f''.join([str(lista) for lista in listas]))
listas.reverse()

for lista in listas:

    print(lista)



somaemedia=sum(listas)/len(listas)
print(f"A soma dos números é {sum(listas)}") #d
print(f'A média dos 5 números é:{somaemedia}')  #e
print(f''.join([str(lista) for lista in listas if lista>somaemedia]))
print(f''.join([str(lista) for lista in listas if lista<7]))
print("volte sempre! #PYTHON EVERYDAY!")






