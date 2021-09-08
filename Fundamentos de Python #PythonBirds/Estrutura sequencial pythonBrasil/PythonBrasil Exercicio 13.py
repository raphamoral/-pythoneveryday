##Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##Para homens: (72.7*h) - 58
##Para mulheres: (62.1*h) - 44.7
##Using the height (h) of a person as input, build an algorithm to calculate their ideal weight, using the following formulas:
##For men: (72.7*h) - 58
##For women: (62.1*h) - 44.7

altura = float(input("Digite o valor da sua altura : "))

print('''GENERO:
[ 1 ] MASCULINO
[ 2 ] FEMININO
''')

sexo =int(input ("Digite seu numero correspondente ao seu genero  : "))
if(sexo==1) :
    pesoideal= (72.7*altura)-58
if (sexo==2) :
    pesoideal=(62.1*altura)-44.7

print("Seu peso ideal é "+ str(pesoideal) +"kg")