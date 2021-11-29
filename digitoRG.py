class RG ():

    def __init__(self, entrada_numero_rg = None, digito = 0):
        self.digito = digito
        self.entrada_numero_rg = entrada_numero_rg
        
    def calcula_digito(self):
        lista_entrada = []
        multiplicador = 2
        for numero in self.entrada_numero_rg:
            lista_entrada.append(int(numero)*multiplicador)
            multiplicador = multiplicador + 1
        soma_digito = sum(lista_entrada)
        digito_calculado = 11 - ((soma_digito)%11)
        return digito_calculado
         
    def __str__(self):
        if self.digito == 10:
            return 'O dígito verificador do seu rg é X'
        elif self.digito == 11:
            return 'O dígito verificador do seu rg é 0'
        else:
            return 'O dígito verificador do seu Rg é %d' % (self.digito)

def main():
    entrada = input('insira o numero do seu RG sem pontos ou traços \n')
    rg_entrada = RG(entrada)
    digito = rg_entrada.calcula_digito()
    rg = RG(entrada, digito)
    print(rg)

    

if __name__ == '__main__':
    main()


