def validar(ip:str)->bool:
    numeros=ip.split ('.')
    if len (numeros)!=4:
        return False
    for n in numeros:
        if not (0<=int(n)<= 255):
            return  False
    return True
ips_validos=[]
ips_invalidos=[]

with open('sample_data/ips.txt','r')as arquivo:
    for linha in arquivo:
        ip=linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open('sample_data/ips_saida.txt', 'w')as arquivo:
    arquivo.writelines('[Endereços validos:]\n')
    arquivo.writelines('')
    arquivo.writelines('')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')
    arquivo.writelines('[Endereços invalidos:]\n')
    arquivo.writelines('')
    arquivo.writelines('')

    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')



