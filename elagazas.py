import random

number = random.randint(-5,5)
print(number)

if number > 0:
    print('szam pozitiv')
elif number ==0:
    print('szám nulla')
else:
    print('szám negatív')