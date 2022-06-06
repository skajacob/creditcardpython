class CreditCard(): 
    """Se genera la clase CreditCard"""
    def check_credit_card_type(self, creditcard_no):
        """Se genera el metodo  check_credit_card_type este metodo verifica el typo de tarjeta"""
        type=""
        if int(creditcard_no[:2]) in [51, 52, 53, 54, 55 ] and len(creditcard_no) == 16:
            return self.check_credit_card_no(creditcard_no, type="MASTER CARD")
        elif int(creditcard_no[:2]) in [34, 37]:
            return self.check_credit_card_no(creditcard_no, type="AMEX")
        elif len(creditcard_no) == 13 or len(creditcard_no) == 16:
            return self.check_credit_card_no(creditcard_no, type="VISA")
        else:
            return self.check_credit_card_no(creditcard_no, type="VALID")
        
    def check_credit_card_no(self, creditcard_no, type):
        """Se genera el metodo check_credit_card_no verifica si el numero de tarjeta es valido con el algoritmo de Luhn"""
        processed_digits = []
        for digit in creditcard_no:
            creditcard_no=[]
            creditcard_no.append(int(digit))
            double_digit =int(digit)*2
            if double_digit>9:
                double_digit = double_digit-9 
                processed_digits.append(double_digit)
            else:
                processed_digits.append(int(double_digit))
        total_1= sum(creditcard_no[::2]) + sum(processed_digits[1::2])
        total_2= sum(creditcard_no[1::2]) + sum(processed_digits[::2])
        if total_1 % 10 == 0 or total_2 % 10 == 0:
            print(type) 
        else:
            print("INVALID")
    
creditcard_no = input("Insert your credit card number: ").strip()
CreditCard().check_credit_card_type(creditcard_no)   

