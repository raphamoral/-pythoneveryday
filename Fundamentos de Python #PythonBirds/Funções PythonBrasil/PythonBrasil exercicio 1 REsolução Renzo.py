
def imprimir_triangulo_de_numeros(n:int):
    for i in range(1,n+1):
        for _ in range(i):
            print(i, end='   ')
        print('')


numero=int(input(""))
imprimir_triangulo_de_numeros(numero)
