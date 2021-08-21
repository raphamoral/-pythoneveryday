#4.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#4. Assuming that the population of country A is in the order of 80,000 inhabitants with an annual growth rate of 3% and that the population of B is 200,000 inhabitants with a growth rate of 1.5%. Make a program that calculates and writes down the number of years it takes for the population of country A to exceed or equal the population of country B, maintaining the growth rates.
popa=80000
popb=200000
cresca=1.03
crescb=1.015
ano=0
while popa<=popb:
    popa=popa*cresca
    popb=popb*crescb
    ano=ano+1

print(f'A quantidade de anos é {ano}')
print(popb)
print(popa)