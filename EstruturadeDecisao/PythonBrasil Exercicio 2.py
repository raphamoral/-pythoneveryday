#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#Make a Program that asks for a value and shows on the screen whether the value is positive or negative.

number1=float(input("Digite um número negativo ou positivo : "))
print(number1)
if (number1==0):
    print("O numero digitado é neutro ou nulo e tem valor de : " + str(number1))


elif (number1>0):
    print("O numero digitado é positivo e tem valor de : " +str(number1))
elif (number1<0) :
    print("O numero digitado é negativo e tem valor de : " + str(number1))
