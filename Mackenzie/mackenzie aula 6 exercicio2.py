numero =int(input())
while numero <=0:
    print('VALOR INVÁLIDO')
for i in range (1,numero):
    resto= numero%i
    #print(f' resto ={resto}')
    if resto ==0 :
        print(f'{i}', end =' ')
    else:
        pass
    i=+1
