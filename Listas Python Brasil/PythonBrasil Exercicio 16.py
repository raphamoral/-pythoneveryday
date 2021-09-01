#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#Use a list to solve the following problem. A company pays its salespeople on a commission basis. The seller receives $200 a week plus 9 percent of their gross sales for that week. For example, a salesperson who had gross sales of $3000 in one week receives $200 plus 9 percent of $3000, for a total of $470. Write a program (using an array of counters) that determines how many salespeople received salaries in the following ranges of values:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 onwards
salarios=[200,250,320,413,516,680,791,877,999,1000,2000,3000]
contagem_de_salarios= 9*[0]
for salario in salarios:
    indice=salario//100-2
    indice_maximo=(len(contagem_de_salarios) - 1)
    indice=min(indice, indice_maximo)
    contagem_de_salarios[indice] +=1
    print(indice)

print(contagem_de_salarios)