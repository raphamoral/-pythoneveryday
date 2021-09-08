nome=input(str("Digite seu nome")).upper()[::-1]
nome_invertido_por_letras=''.join(reversed(nome))
nome_invertido_por_palavras= ''.join((reversed(nome.split())))
reverso=nome
print(f'Nome invertido por palavras :{nome_invertido_por_palavras}')

print(nome_invertido_por_letras)
print(reverso)
