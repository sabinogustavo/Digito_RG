from document import Document

class CPF(Document):
        
    def digit_calculator(self):
        
        input_list_first_digit = []
        input_list_second_digit = []
        multiplier_first_digit = 1
        multiplier_second_digit = 0

        for num in self.number:
            input_list_first_digit.append(int(num)*multiplier_first_digit)
            multiplier_first_digit = multiplier_first_digit + 1
        first_digit_sum = sum(input_list_first_digit)
        calculated_first_digit =(first_digit_sum)%11

        for num in self.number:
            input_list_second_digit.append(int(num)*multiplier_second_digit)
            multiplier_second_digit = multiplier_second_digit + 1
        second_digit_sum = sum(input_list_second_digit) + (calculated_first_digit*9)
        calculated_second_digit =(second_digit_sum)%11
        
        if calculated_second_digit >= 10:
            second_digit = 0
        else:
            second_digit = calculated_second_digit
        
        if calculated_first_digit >= 10:
            first_digit = 0
        else:
            first_digit = calculated_first_digit
    
        return f'{first_digit}' + f'{second_digit}'
        

    
    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        return f'O número do seu CPF, com o dígito, é: {self.number[0:3]}.{self.number[3:6]}.{self.number[6:]}-{self.digit}'

