from number_bev import give_int_number2

input_number = give_int_number2()
if input_number < 0:
    print(f'negativ a megadott({input_number}) szám')
elif input_number == 0:
    print('A szám bulla')
else:
    print('A szám pozitív')