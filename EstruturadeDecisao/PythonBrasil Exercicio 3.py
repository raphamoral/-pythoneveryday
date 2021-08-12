# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Make a Program that checks whether a typed letter is "F" or "M". As the letter writes: F - Female, M - Male, Invalid Sex.
letter = (input("Digite F  seu sexo é feminino ou M se é masculino : "))
if letter == "M":
    print("O seu sexo é masculino")
if letter == "F":
    print("O seu sexo é feminino")
if (letter!="M"and letter!="F") :
    print("Sexo invalido")
