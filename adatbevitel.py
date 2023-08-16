def give_int_number():
    is_number = False
    while is_number==False:
        give_word = input('Adj meg egy számot:')    
        try:
            number = int(give_word)       
        except ValueError:
            print('Nem int szám lett megadva')
            #pass
        else:
            is_number = True
    return  number

def _give_int_number2():
    is_number = False
    while is_number==False:
        try:
            number=int(input('adj meg egy int number:'))
        except ValueError:
            print('Nem szám lett megadva')
        else:
            is_number = True
    return  number


def kiir(number):
    for i in range(0,10):
        print('*'*(i+1),end='\n')

#print(_give_int_number2())
# give_word = input('Add meg egy számot:')
# print(type(give_word))
# print(int(give_word)/2)
# number = int(give_word)/2
# print(f"A szám fele:{number}")

szam1 = 10
szam2 = 20
szam3 = 30
print(szam1,szam2,szam3,sep='    ')
print('*'*5)
kiir(10)
