#Faça um Programa que leia três números e mostre-os em ordem decrescente.
#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1=float(input("Digite o valor do primeiro numero : "))
n2=float(input("Digite o valor do segundo numero: "))
n3=float(input("Digite o valor do terceiro numero: "))

if n1>n2>n3:
    print ( " O Valor decrescente é "+ str(n1) +">"+ str(n2) +">"+ str(n3))
elif n1>n3>n2 :
    print(" O Valor decrescente é " + str(n1) + ">" + str(n3) + ">" + str(n2))
elif n3>n2>n1:
    print(" O Valor decrescente é " + str(n3) +">"+ str(n2) +">"+ str(n1))
elif n3>n1>n2 :
    print(" O Valor decrescente é " + str(n3) + ">" + str(n1) + ">" + str(n2))
elif n2>n1>n3:
    print(" O Valor decrescente é " + str(n2) +">"+ str(n1) +">"+ str(n3))
elif n2>n3>n1 :
    print(" O Valor decrescente é " + str(n2) + ">" + str(n3) + ">" + str(n1))
elif n1==n2==n3:
    print(" todos os numeros são iguais")
elif n3==n1 and n2>n1 :
    print(" O valor maior é " +str(n2)+" E os demais valores são iguais a" +str(n1) +"e a ordem é " +str(n3)+">"+str(n1))
elif n1==n2 and n3>n1 :
    print(" O valor maior é " +str(n3)+" E os demais valores são iguais a" +str(n1) +"e a ordem é " +str(n3)+">"+str(n1))
elif n2==n3 and n1>n3 :
    print(" O valor maior é " +str(n1)+" E os demais valores são iguais a" +str(n3) +"e a ordem é " +str(n1)+">"+str(n3))
