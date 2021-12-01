from document import Document

class CNPJ(Document):
        
    def digit_calculator(self):
        input_list = []
        multiplier = 2
        for num in self.number:
            input_list.append(int(num)*multiplier)
            multiplier = multiplier + 1
        digit_sum = sum(input_list)
        calculated_digit = 11 - ((digit_sum)%11)
        print(calculated_digit)
        return calculated_digit

    
    def __str__(self):
        if self.digit == 10:                                                                                                                                            
            return f'O número do seu documento, com o dígito, é: {self.number[0:2]}.{self.number[2:5]}.{self.number[5:]}-X'
        elif self.digit == 11:                                                                                          
            return f'O número do seu documento, com o dígito, é: {self.number[0:2]}.{self.number[2:5]}.{self.number[5:]}-0'
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            return f'O número do seu documento, com o dígito, é: {self.number[0:2]}.{self.number[2:5]}.{self.number[5:]}-{self.digit}'

 
