entradaNumRG = input('insira o numero do seu RG sem pontos ou traços \n')

def multiplicadorEntrada(entradaNumRG):
    listaEntrada = []
    multiplicador = 2
    for numero in entradaNumRG:
        listaEntrada.append(int(numero)*multiplicador)
        multiplicador = multiplicador + 1
    return listaEntrada    
    
def saidaDigitoVer(digitoVer):
    if digitoVer == 10:
        print ('O dígito verificador do seu rg é X')
    elif digitoVer == 11:
        print ('O dígito verificador do seu rg é 0')
    else:
        print('O dígito verificador do seu Rg é %d'%digitoVer)

digitoVer = 11 - (sum(multiplicadorEntrada(entradaNumRG))%11)

saidaDigitoVer(digitoVer)
