from document import Document

class RG(Document):
        
    def digit_calculator(self):
        input_list = []
        multiplier = 2
        for num in self.number:
            input_list.append(int(num)*multiplier)
            multiplier = multiplier + 1
        digit_sum = sum(input_list)
        calculated_digit = 11 - ((digit_sum)%11)
        
        if calculated_digit == 10:
            return 'X'
        elif calculated_digit == 11:
            return 0
        else:
            return calculated_digit

    
    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        return f'O número do seu RG, com o dígito, é: {self.number[0:2]}.{self.number[2:5]}.{self.number[5:]}-{self.digit}'


