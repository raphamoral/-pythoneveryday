##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
##Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary for that month.


a=(float (input ("Quanto você recebe por hora ?  ")))
b=(float (input ("Quantas horas você trabalha no mês? ")))
c=(float (input ("Quantos minutos você trabalha no mês alem das horas ? ")))
minutdec= c/60

d= a*(minutdec+b)
print (" O valor mensal que você recebe é " + str(d))
print(f'O valor mensal que voce recebe é {d}')
   

