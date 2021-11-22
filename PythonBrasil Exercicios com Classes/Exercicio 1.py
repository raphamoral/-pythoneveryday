class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferiencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return id(self)
    def troca_cor(self,cor):
        self.cor=cor

    pass
circulo_primeiro=CirculoPerfeito()
circulo_segundo=CirculoPerfeito()

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())