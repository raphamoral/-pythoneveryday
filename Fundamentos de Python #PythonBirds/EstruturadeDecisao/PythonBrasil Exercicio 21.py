import math
textnota1=""
retirada=int(input("Digite o valor que deseja retirar : "))

if 600>=retirada>=1:
    centenas=math.floor(retirada/100)
    if centenas==0:
        textnota100=""
    else:
        textnota100=("Numero de notas de 100 ="+str(centenas))

    dezenas=math.floor((retirada-centenas*100)/10)
    if dezenas >=5:
        nota50=1
        nota10=dezenas-5
        textnota10=("\n notas de 10=" +str(nota10))
        textnota50=("\n Notas de 50 =" +str(nota50))
        if nota10==0:
            textnota10=""
        else:
            textnota10 = ("\n notas de 10=" + str(nota10))
    else:
        textnota50 = ""
        nota10=dezenas
        if nota10==0:
            textnota10=""
        else:
            textnota10 = ("\n notas de 10=" + str(nota10))

    unidades=retirada-dezenas*10-centenas*100
    if unidades >5:
        nota5=1
        nota1=unidades-nota5*5
        textnota5 = ("\n nota de 5 = " + str(nota5))
        textnota1 = ("\n Notas de 1 = " + str(nota1))
    if unidades==5:
        nota5 = 1
        textnota5 = ("\n nota de 5 = " + str(nota5))
        textnota1=""
    if unidades<5:
        nota1=unidades
        nota5=0
        textnota5=""
        textnota1 = ("\n Notas de 1 = " + str(nota1))
        if nota1 == 0:
            textnota1 = ""
    print(textnota100+textnota50+textnota10+textnota5+textnota1)
else :
    print("Numero inválido")