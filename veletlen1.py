import random

class Randomnumber1:
    def __init__(self, value):
        self.value = value
        self.random = None

    def get_random_number(self):
        self.random = random.randint(1,2)

    def check_the_input_and_random(self):
        if self.random != None:
            if self.random != self.value:
                print("A bekért és a véletlen szám nem egyezik")
                print(self.value)
                print(self.random)
            else:
               
                print("A bekérté és véletlen szám egyezik!!!!!")
        else:
            print("A random szám még nem lett generálva")

def request_number_from_user(text):
    number_is_good = False
    while number_is_good == False:
        try:
            number=int(input(text))                    
        except Exception as e:
            pass
        else:
            number_is_good = True            
    return number

#random_number = random.randint(1,100)
#print(random_number)

#a = request_number_from_user('Adjon meg egy számot:')
#randum_number = random.randint(1,2)

t = Randomnumber1(request_number_from_user('Adjon meg egy számot:'))
t.get_random_number()
t.check_the_input_and_random()