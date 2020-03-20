#FORR1FG05AU-Hát - Skilaverkefni 3 - Liður 3 - Steinn Þorkelsson

import time
leyniord = input('Hvað er leyniorðið?: ')
if leyniord == "salat":
    print('Velkominn')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('Vinsamlegast farðu úr skónnum')
    time.sleep(0.5)
while leyniord != "salat":
    print('Vitlaust')
    time.sleep(0.5)
    leyniord = input('Hvað er leyniorðið?: ')
    if leyniord == "salat":
        print('Velkominn')
        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        print('Vinsamlegast farðu úr skónnum')
        time.sleep(0.5)
