tab =int(input())
while tab <=0:
    print('VALOR INVÁLIDO')
    tab = int(input())
for num in range (1,11,1):
    resultado= num*tab
    print (f'{tab}x{num}={resultado}')