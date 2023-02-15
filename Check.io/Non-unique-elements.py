from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    # listaB=[listaB.append(i) for i in data if data.count(i)>1]
    listaB=[]
    for i in data:
        contador=data.count(i)
        if contador>1:
            listaB.append(i)


    # your code here
    return listaB


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
