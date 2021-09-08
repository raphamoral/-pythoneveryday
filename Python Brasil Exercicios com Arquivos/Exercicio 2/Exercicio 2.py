lista_de_dados=[]
def transformar_em_megabytes (tamanho_em_bytes : str) -> float:
    return float(tamanho_em_bytes/(2**10)**2)



with open('data/usuarios.txt', mode='r') as arquivoss:

    for linha in arquivoss:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(float(linha[16:]))




        lista_de_dados.append((usuario,tamanho_em_disco))

#print(lista_de_dados)

cabecalho='''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n'''


with open('data/relatorio.txt', mode='w') as arquivoss:

    tamanho_total_consumido = (sum(tamanho for _, tamanho in lista_de_dados))
    media=tamanho_total_consumido/len(lista_de_dados)
    arquivoss.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario,tamanho_em_disco=dados
        arquivoss.writelines(f'{indice:<3}  {usuario} {tamanho_em_disco:8.2f} MB        {tamanho_em_disco / tamanho_total_consumido:>8.2%} \n'
                             )

    arquivoss.writelines(f"O total de tamanho total consumido é:{tamanho_total_consumido:.2f}MB\n")
    arquivoss.writelines(f'A media de consumo é:{media:.2f}MB')

