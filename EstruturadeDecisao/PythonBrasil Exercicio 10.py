#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
#Make a Program that asks which shift you study. Ask to enter M-Morning or V-Evening or N-Night. Print the message "Good morning!", "Good afternoon!" or good night!" or "Invalid Value!", as appropriate.
letter = (input("Digite M para o periodo maturtino, digite V para Vespertino e N para noturno : ")).upper()
if letter == "M":
    print("O seu periodo é  maturtino . Bom dia !")
elif letter == "V":
    print("O seu periodo é vespetino. Boa Tarde!")
elif letter == "N":
    print("O seu periodo é  noturno . Boa noite!")
else:
    print ("Periodo inválido")