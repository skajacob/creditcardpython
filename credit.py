class CreditCard(): 
    """Se genera la clase CreditCard"""        
    def check_credit_card_no(self, creditcard_no):
        """Se genera el metodo check_credit_card_no verifica si el numero de tarjeta es valido con el algoritmo de Luhn"""
        type_card = {
            '51' : 'MASTER CARD',
            '52' : 'MASTER CARD',
            '53' : 'MASTER CARD',
            '54' : 'MASTER CARD',
            '55' : 'MASTER CARD',
            '34' : 'AMEX',
            '37' : 'AMEX',
            '41' : 'VISA',
            '42' : 'VISA',
            '47' : 'VISA',
        }
        if len(creditcard_no) == 13 or len(creditcard_no) == 16:
            processed_digits = []
            creditcard_no_list = []
            for digit in creditcard_no:
                creditcard_no_list.append(int(digit))
                double_digit =int(digit)*2
                if double_digit>9:
                    double_digit = double_digit-9 
                    processed_digits.append(double_digit)
                else:
                    processed_digits.append(int(double_digit))
            total_1= sum(creditcard_no_list[::2]) + sum(processed_digits[1::2])
            total_2= sum(creditcard_no_list[1::2]) + sum(processed_digits[::2])
            if total_1 % 10 == 0 or total_2 % 10 == 0:
                print(format(type_card[creditcard_no[:2]])) 
        else:
            print("INVALID")
    
creditcard_no = input("Insert your credit card number: ").strip()
CreditCard().check_credit_card_no(creditcard_no)    


