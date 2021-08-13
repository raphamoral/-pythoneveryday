##Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
##Make a program for a paint shop. The program should ask for the size in square meters of the area to be painted. Consider that the paint coverage is 1 liter for every 3 square meters and that the paint is sold in 18 liter cans, which cost R$ 80.00. Inform the user of the quantities of paint cans to be purchased and the total price.

import math
metrosquadradados= float(input("Digite o valor da área em metros quadrados a ser pintado:"))
litrosparametros= metrosquadradados / 3
precolata=80
litroslata=18
if (litrosparametros > litroslata) :
    precofinal1= (math.ceil(litrosparametros / litroslata)) * precolata
else:
    precofinal1 =precolata
print("o preço final é R$ : " + str(precofinal1))
