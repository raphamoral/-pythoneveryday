#Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em determinada cidade. Para isso, são fornecidos os seguintes dados:

#o preço de KW/hora consumido;
#a quantidade de KW/hora consumida durante o mês/ e
#o tipo de consumidor (Industrial, Comercial, Residencial).


#Dependendo do tipo de consumidor, a conta mensal sofre um acréscimo:

#industrial – 15%;
#comercial – 5%;
#residencial – não tem acréscimo.

while True:
    try:
        preço_de_kw_hora =float(input("Digite o valor do preço de KW/hora consumido : "))
        quantidade_consumida=float(input("Digite a quantidade de KW/hora consumida no mês :"))
        tipo_de_consumidor=str(input("Digite o tipo de consumidor : industrial,comercial ou residencial : ")).upper()

        if tipo_de_consumidor=='INDUSTRIAL'or'COMERCIAL'or'RESIDENCIAL':
            if tipo_de_consumidor== 'INDUSTRIAL':
                valor_da_conta=float(preço_de_kw_hora*quantidade_consumida*1.15)
            elif tipo_de_consumidor == 'COMERCIAL':
                valor_da_conta =float( preço_de_kw_hora * quantidade_consumida * 1.05)
            elif tipo_de_consumidor =='RESIDENCIAL':
                valor_da_conta =float(preço_de_kw_hora * quantidade_consumida)

        print(f"O Valor da conta mensal do consumidor é :{valor_da_conta}")
        break
    except ValueError:
        print('Deve ser fornecido um valor valido')
    except NameError:
        print("Escreva corretamente o tipo de consumidor")
