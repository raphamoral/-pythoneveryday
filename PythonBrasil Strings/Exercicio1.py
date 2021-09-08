s1='Hexa'
s2='Hexa!'
tamanho1=len(s1)
tamanho2=len(s2)

print(f'{s1}:{tamanho1}caracteres')
print(f'{s2}:{tamanho2} caracteres')
comparação_de_tamanho='diferentes'
comparação_de_conteudo='diferente'
if s1==s2:
    comparação_de_tamanho = 'iguais'
    comparação_de_conteudo = 'igual'
elif tamanho1==tamanho2:
    comparação_de_tamanho='iguais'
print(f"As duas strings são de tamanho {comparação_de_tamanho}")
print(f'As duas strings possuem conteudo {comparação_de_conteudo}')
