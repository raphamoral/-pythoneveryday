def nearest_value(values: set, one: int) -> int:

    lista =[]
    lista2=[]
    if one in values:
        return one
    values =list(values)
    for i in range(values):
        if (values[i]-one)>0:
            lista.append(values[i])
            for j in range(lista):
                if (lista[j]-one)< lista[j-1] -one:
                    lista2.append(lista[j])
                elif lista[j]-one ==lista[j-1]-one:
                    lista2.append(lista[j-1])




if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
