##João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
##João Papo-de-Pescador, a good man, bought a microcomputer to control the daily income of his work. Every time he brings a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos), he must pay a fine of R$ 4.00 per excess kilo. John needs you to make a program that reads the variable weight (weight of fish) and calculates the excess. Record in the excess variable the amount of kilos over the limit and in the fine variable the amount of the fine that João must pay. Print out the program data with the appropriate messages.
peso=float(input("por favor insira o valor do peso total de peixes :"))
if (peso>50) :
   excesso= peso - 50
   multa= excesso * 4
else :
   excesso=0
   multa=0

print("A quantidade de quilos em excesso é : " +str(excesso)+"kg" )
print("o Valor da multa é : ""R$" +str(multa))