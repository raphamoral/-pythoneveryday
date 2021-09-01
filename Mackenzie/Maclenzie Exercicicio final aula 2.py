#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar: a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado. b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. Observe que as quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites deve ser arredondada para cima, usando a função matemática apropriada em Python.ython.
import math
valordoespetaculo=(float(input("")))# Digite o valor do espetaculo
precodoconvite=(float(input((""))))#Digite o valor do preço convite
numerodeconvites=math.ceil(valordoespetaculo/precodoconvite)
lucro23=math.ceil(1.23*valordoespetaculo/precodoconvite)
print(numerodeconvites)
print(lucro23)
