class Quadrado:
    def __init__(self,lado = 1):
        self.lado=lado
    def calcular_area(self):
        return self.lado**2
quadrado=Quadrado(4)
print (quadrado.lado,quadrado.calcular_area())
