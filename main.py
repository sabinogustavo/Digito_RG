from document import Document
from rg import RG
from cpf import CPF

def main():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    document_input = input('insira o numero do seu documento sem pontos ou traços \n') 
    
    try:
        len(document_input) == 8
        try:
            len(document_input) == 9
        except:
            'insira o número do seu documento sem pontos ou dígito'     
    finally:
        if len(document_input) == 8:
            rg = RG()
            rg.number = document_input
            rg.digit = rg.digit_calculator()
            print(rg)    
        elif len(document_input) == 9:
            cpf = CPF()
            cpf.number = document_input
            cpf.digit = cpf.digit_calculator()
            print(cpf)  

if __name__ == '__main__':
    main()

