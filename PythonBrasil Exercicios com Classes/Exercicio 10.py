class Bomba_De_Combustivel ():
    def __init__(self,tipo_combustivel:str,valor_litro:float,quantidade_combustivel:float):

        self.tipo_combustivel= tipo_combustivel
        self.valor_litro =valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    def abastecer_por_valor(self, valor:float):

        litros_abastecidos = valor/ self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos,valor)
    def _apresentar_abastecimento_se_possivel (self, litros_abastecidos : float ,valor :float):
        if litros_abastecidos >self.quantidade_combustivel:
            print(f'Não é possível abastecer, faltam {litros_abastecidos- self.quantidade_combustivel:.2f} litros.')
            print('Reabasteça a bomba')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f' A quantidade de litros abastecidos é {litros_abastecidos} a um valor de{valor:.2f}')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')
    def abastecer_por_litros (self, litros_abastecidos :float):
        valor=litros_abastecidos*self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)
    def adicionar_mais_combustivel (self, quantidade:float):
        if quantidade >=0:
            self.quantidade_combustivel +=quantidade
        else:
            print('Eai malandro, tá tirando onda, corre que a policia já está chegando')





bomba =Bomba_De_Combustivel('Gasolina',4.59,100.0)
bomba.abastecer_por_valor(100)
bomba.abastecer_por_litros(50)
bomba.valor_litro = 5.59
bomba.abastecer_por_litros(50)
bomba.adicionar_mais_combustivel (100)
bomba.abastecer_por_litros(50)
bomba.adicionar_mais_combustivel(-100)