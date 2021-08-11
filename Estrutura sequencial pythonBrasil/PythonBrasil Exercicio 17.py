##Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
##Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
##comprar apenas latas de 18 litros;
##comprar apenas galões de 3,6 litros;
##misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
squaremeters= float(input( "Digite o valor da área em metros quadrados a ser pintado:"))
pricebiglat= 80.00
pricesmalllat= 25.00
lbiglat=18
biglat=18
lsmalllat=3.6
smalllat=3.6
llat=squaremeters/6
print("total em litros : "+str(llat) + "l")
llat1=llat*1.1

if (llat==0):
    pricefin4= 0
    print("Preço inválido, recomece novamente")
    
if (llat > lbiglat) :
    pricefin= (math.ceil(llat/lbiglat))*pricebiglat
else:
    pricefin =pricebiglat

if (llat > lsmalllat):
    pricefin2=(math.ceil(llat/smalllat))*pricesmalllat
else :
    pricefin2=pricesmalllat
            
    

tblat=(math.floor(llat1/biglat)) 
resto =((llat1/biglat)-tblat)*biglat
if (resto < 10.8):
    tg= math.ceil(resto/smalllat)
else :
    tg=pricebiglat/pricesmalllat  
    
mix= tg*pricesmalllat +pricebiglat*tblat
    
print(" O valor para compra de somente de latas de 18 l é : R$" + str(pricefin))
print ("O valor para compra de somente galões de 3.6 l é : R$" + str(pricefin2))
print ("O valor para mistura de galões e latas com 10 por cento de acréscimo é : R$" +str(mix))  
               
        
