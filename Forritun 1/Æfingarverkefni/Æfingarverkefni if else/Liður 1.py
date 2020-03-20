"""Forritið biður notanda um tvær heiltölur.
Forritið skrifar síðan út hvor talan er minni.
Ef tvisvar er slegin inn sama talan á forritið að skrifa “Tölurnar eru jafn stórar”.
"""
x = int(input('Tala 1: '))
y = int(input('Tala 1: '))
if x < y:
    print('Minni talan er:', x)
elif x > y:
    print('Minni talan er:', y)
else:
    #print('Tölurnar eru jafn stórar:', x,'og', y)
    print(f'Tölurnar {x} og {y} eru jafn stórar.')