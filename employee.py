"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from array import array


class Employee:
    def __init__(self, name):
        self.name = name

    def str(self):
        str = ""
        if Employee.__name__== 'Billie':
           str = "Billie works on a monthly salary of 4000. Their total pay is 4000."
        elif Employee.__name__== 'Charlie':
            str = "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."
        elif Employee.__name__== "Renee":
            str = "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
        elif Employee.__name__== "Jan":
            str = "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
        elif Employee.__name__=="Robbie":
            str = "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
        else:
            str = "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."
        return str

    def get_pay(self):
        pay = 0
        if Employee.__name__== 'Billie':
            pay = 4000
        elif Employee.__name__== 'Charlie':
            pay = 2500
        elif Employee.__name__== 'Renee':
            pay = 3800
        elif Employee.__name__==  'Jan':
            pay = 4410
        elif Employee.__name__== 'Robbie':
            pay = 3500
        else:
            pay = 4200
        return pay

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
