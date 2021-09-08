##Faça um Programa que peça as 4 notas bimestrais e mostre a média
##Make a Program that asks for the 4 bimonthly notes and shows the average.
a=0
while True:
    try:
        nota = float(input("Informe a nota entre 0 e 10 do primeiro bimestre: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    
        
    try:
        nota2 = float(input("Informe a nota entre 0 e 10 do segundo bimestre: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    
        
    try:
        nota3 = float(input("Informe a nota entre 0 e 10 do terceiro bimestre: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
   
        
    try:
        nota4 = float(input("Informe a nota entre 0 e 10 do quarto bimestre: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    
        
    media = (nota+nota2+ nota3+ nota4)/4
    print(media)
    break
