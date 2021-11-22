values=({4, 7, 10, 11, 12, 17}, 9)
lista =values[0]
one =values[1]
x=1

if one in lista:
    print(one)
else:
    for x in range(len(lista)):
        valoratual=lista[x]
        valorproximo=lista[x+1]

        if one > valoratual:
            if valorproximo < one:
                if (valorproximo - one) > (valoratual - one):
                    list.append(valorproximo)
                else:
                    list.append(valoratual)
            else:
                    pass
print(max(list))
