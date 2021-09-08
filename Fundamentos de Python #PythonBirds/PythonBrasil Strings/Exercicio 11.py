from random import choice

lista = ['Amarelo',
         'Amiga',
         'Amor',
         'Ave',
         'Avião',
         'Avó',
         'Balão',
         'Bebê',
         'Bolo',
         'Branco',
         'Cama',
         'Caneca',
         'Celular',
         'Clube',
         'Copo',
         'Doce',
         'Elefante',
         'Escola',
         'Estojo',
         'Faca',
         'Foto',
         'Garfo',
         'Geleia',
         'Girafa',
         'Janela',
         'Limonada',
         'Mãe',
         'Meia',
         'Noite',
         'Óculos',
         'ônibus',
         'Ovo',
         'Pai',
         'Pão',
         'Parque',
         'Passarinho',
         'Peixe',
         'Pijama',
         'Rato',
         'Umbigo']

sorteio=(choice(lista))
palavra=sorteio.upper()
numero_de_caracteres=len(palavra)
conjunto_letras_palavra=set(palavra)
conjunto_letras_digitadas=set()

for letra in palavra:
    print(f'_ ', end=' ')
erros=0

while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas) and erros<7:
    print()
    print()
    letra_digitada=input('Digite uma letra').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavra:
        print('A palavra é:', end='')
        for letra in palavra:

                if letra in conjunto_letras_digitadas:
                    print(f'{letra}',end=' ')
                else:
                    print('_ ', end='')
    else:
        erros+=1
        print(f'->Erros{erros} de 6.Tente de novo!')

    print()
    print('Letras já digitadas:', conjunto_letras_digitadas)
if erros<7:
    print("parabens")
else:
    print('Voce perdeu')



#letra_digitada =input('Digite uma letra: ')
#while tentativas=<6:
#    c=input(string("Digite uma letra:").upper
#    for pos, char in enumerate(sorteio_m):
##        if (char == c):
#            lst.append(pos)
#                if letra nao pertence a sorteio:
#                    tentativas+=1
#                else:


