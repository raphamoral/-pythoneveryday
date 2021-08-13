##Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
##Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
##comprar apenas latas de 18 litros;
##comprar apenas galões de 3,6 litros;
##misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math



precolata= 80.00
precogalao= 25.00
litroslata=18

litrosgaloes=3.6

metrosquadradados= float(input("Digite o valor da área em metros quadrados a ser pintado:"))
litrosparametros= metrosquadradados / 6
print("total em litros : " + str(litrosparametros) + " L")
litrosparametros11= litrosparametros * 1.1
#while true :
    #litrosparametros<=0 :
    #if litrosparametros >0:
    #    break
   # print ('type a valid number')

##    pricefin4= 0
##    print("Preço inválido, recomece novamente")
##    break

while litrosparametros11<=0:
    print("Digite um número válido da proxima vez")
    if litrosparametros11>0:

        break


if (litrosparametros > litroslata) :
    precofinal1= (math.ceil(litrosparametros / litroslata)) * precolata
else:
    precofinal1 =precolata

if (litrosparametros > litrosgaloes):
    precofinal2= (math.ceil(litrosparametros / litrosgaloes)) * precogalao
else :
    precofinal2=precogalao
            
    

quantidadelatas =(math.floor(litrosparametros11 / litroslata))
resto = ((litrosparametros11 / litroslata) - quantidadelatas) * litroslata
if (resto < 10.8):
    totalgaloes= math.ceil(resto / litrosgaloes)
else :
    totalgaloes= precolata / precogalao
    
mix= totalgaloes * precogalao + precolata * quantidadelatas
    
print(" O valor para compra de somente de latas de 18 l é : R$" + str(precofinal1))
print ("O valor para compra de somente galões de 3.6 l é : R$" + str(precofinal2))
print ("O valor para mistura de galões e latas com 10 por cento de acréscimo é : R$" +str(mix))
               
        
