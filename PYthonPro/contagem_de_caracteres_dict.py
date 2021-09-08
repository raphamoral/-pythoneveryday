def contar_caracteres(s):
    """
    Função que conta caracteres de uma string
    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    :param s: string a ser contada

    """

    resultado={}
    for caracter in s:
        resultado[caracter]= resultado.get(caracter,0)+1

    return resultado


if __name__ == '__main__':
   print( contar_caracteres('raphael'))

   print(contar_caracteres('moral'))
