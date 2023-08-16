szoveg = 'Ez egy hosszú szöveg'
szam : int = 2
PI = 3.14
_hosszabb_szoveg_valmai='szoveg leírása'
# print(szoveg)
# print(szam)
# print(szam*PI)
# test_string = 'Ez egy szoveg:{name}'
# szoveg=test_string.format(name='valami2')
test1='Első szöveg helye:{2}, második szöveg helye:{1},harmadik szöveg helye:{0}'
test2=test1.format('Első','második','harmadik')
oszhatosag=True
print(test2)
print(type(szam))
print(type(oszhatosag))
egy_szoveg_szam='17.8'
real_number = float(egy_szoveg_szam)
print(real_number)