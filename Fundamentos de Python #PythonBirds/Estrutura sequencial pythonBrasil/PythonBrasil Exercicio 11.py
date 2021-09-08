##Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
##o produto do dobro do primeiro com metade do segundo .
##a soma do triplo do primeiro com o terceiro.
##o terceiro elevado ao cubo
a= (int(input(" Insira um valor inteiro  : ")))
b= (int(input(" Insira outro valor inteiro : ")))
c= (float(input(" Insira um valor real: ")))

cont1=a*b
cont2=3*a+ 3*b
cont3=c**3
print(" O primeiro valor é " +str(cont1))
print (" O segundo valor é " +str(cont2))
print(" O terceiro valor " + str(cont3))
