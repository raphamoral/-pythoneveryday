#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

#Make a program for reading two partial notes from a student. The program must calculate the average achieved per student and present:
#The message "Approved", if the achieved average is greater than or equal to seven;
#The message "Failed" if the average is less than seven;
#The message "Approved with Distinction" if the average equals ten.
n1=float(input("Digite o valor da primeira nota : "))
n2=float(input("Digite o valor da segunda nota : "))

media= (n1+n2)/2

if media==10:
    print("Aprovado com Disitinção")
if 10>media>=7:
    print("Aprovado")
if media<7 :
    print("Reprovado")

