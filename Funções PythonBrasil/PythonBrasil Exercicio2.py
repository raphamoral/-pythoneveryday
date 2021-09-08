def imprimir_trinagulo_de_numeros_crescente(n):
    for linha in range(1, n + 1):
        for coluna in range(1,linha+1):
            print(coluna, end='   ')
        print('')


numero = int(input(""))
imprimir_trinagulo_de_numeros_crescente(numero)
