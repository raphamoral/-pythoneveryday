##Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
##Using a person's height as input data, build an algorithm that calculates their ideal weight using the following formula: (72.7*height) - 58

altura = float(input("Digite o valor da sua altura : "))
pesoideal=(72.7*altura)-58
print("Seu peso ideal é:"+ str(pesoideal) + ("kg"))