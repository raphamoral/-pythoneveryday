##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
##salário bruto.
##quanto pagou ao INSS.
##quanto pagou ao sindicato.
##o salário líquido.
##calcule os descontos e o salário líquido, conforme a tabela abaixo:
##+ Salário Bruto : R$
##- IR (11%) : R$
##- INSS (8%) : R$
##- Sindicato ( 5%) : R$
##= Salário Liquido : R$
##Obs.: Salário Bruto - Descontos = Salário Líquido.

##Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary for that month, knowing that 11% is deducted for Income Tax, 8% for INSS and 5% for the union, make a program that gives us:
##gross salary.
##how much you paid the INSS.
##how much you paid the union.
##the take-home pay.
##calculate discounts and net salary, as shown in the table below:
##+ Gross Salary: R$
##- Income Tax (11%): R$
##- INSS (8%): ​​R$
##- Union (5%): R$
##= Net Salary: R$
##Note: Gross Salary - Discounts = Net Salary.
a=(float (input ("Quanto você recebe por hora ?  ")))
b=(float (input ("Quantas horas você trabalha no mês? ")))
c=(float (input ("Quantos minutos você trabalha no mês alem das horas ? ")))
minutdec= c/60

d= a*(minutdec+b)
salariobruto=d
ir=salariobruto*0.11
inss=salariobruto*0.08
sindicato=salariobruto*0.05
descontos= ir+inss+sindicato
salarioliquido=salariobruto-descontos
print("O valor do salario bruto é : R$"+str(salariobruto))
print("O valor do IR é : R$"+str(ir))
print("O valor do inss é : R$"+str(inss))
print("O valor do sindicato é : R$"+str(sindicato))
print("O valor dos descontos é : R$"+str(descontos))
print("O valor do salario liquido é é : R$"+str(salarioliquido))