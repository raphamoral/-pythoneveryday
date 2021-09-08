##Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
##Make a Program that checks whether a typed letter is a vowel or a consonant.
letter = (input("Digite uma letra para decifrarmos se é consoante ou vogal : ")).upper()
print(letter)
x=letter.isalpha()
while x==False:
    #print("Caractere inválido")
    if x==True:
        break
   ## print("Caractere inválido")

if letter!="A" and letter!="E"and letter!="I" and letter!="O"and letter!="U":
    print(" Isso é uma consoante")
else:
    print("Isso é uma vogal")