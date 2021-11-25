entradaNumRG = input('insira o numero do seu RG sem pontos ou traços \n')
listaEntrada = []
multiplicador = 2

for numero in entradaNumRG:
    listaEntrada.append(int(numero)*multiplicador)
    multiplicador = multiplicador + 1
    

somaNumRG = sum(listaEntrada)

digitoVer = 11 - (somaNumRG%11)

if digitoVer == 10:
    print ('O dígito verificador do seu rg é X')
elif digitoVer == 11:
    print ('O dígito verificador do seu rg é 0')
else:
    print('O dígito verificador do seu Rg é %d'%digitoVer)
