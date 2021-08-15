#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
#The Tabajara Organizations decided to give their employees a salary increase and hired him to develop the program that will calculate the adjustments.
#Make a program that receives an employee's salary and readjusts it according to the following criteria, based on the current salary:
#salaries up to R$ 280.00 (including): 20% increase
#salaries between BRL 280.00 and BRL 700.00: 15% increase
#salaries between R$ 700.00 and R$ 1500.00: 10% increase
#salaries from R$ 1500.00 onwards: 5% increase After the increase is carried out, inform on the screen:
#the salary before the readjustment;
#the percentage of increase applied;
#the amount of the increase;
#the new salary, after the increase.
salario=float(input("Digite o valor do seu salário : "))

if salario<280 :
    salarionovo=salario*1.2
elif 700>=salario>280:
    salarionovo=salario*1.15
elif 1500>salario>700:
    salarionovo=salario*1.10
elif salario>=1500:
    salarionovo=salario*1.05
elif salario<=0:
    print(" valor inválido")
    salarionovo=0
else:
    print("valor inválido")
aumento= salarionovo-salario
percentual=((salarionovo/salario)-1)*100

print("o valor do seu salário antes do reajuste é : R$ " + str(salario) )
print ( " o valor do seu salario novo é R$" + str(salarionovo) )
print(" O percentual de aumento aplicado é "+str(percentual)+" %")
print (" O valor do aumento é R$" + str(aumento))
