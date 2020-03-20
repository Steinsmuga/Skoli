#FORR1FG05AU-Hát - Tímaverkefni 1 - A - Steinn Þorkelsson
import random
tala = random.randint(0, 100)
gisk = int(input("Giskaðu á tölu frá 0 - 100: "))
tilraunir = 1
while tala != "guess":
    if gisk < tala:
        print("Of Lágt")
        tilraunir = tilraunir + 1
        gisk = int(input("Giskaðu aftur: "))
    elif gisk > tala:
        print("Of Hátt")
        tilraunir = tilraunir + 1
        gisk = int(input("Giskaðu aftur: "))
    else:
        print(f'Hárrétt!!! það tók þig {tilraunir} tilraunir að ná svarinu')
        break