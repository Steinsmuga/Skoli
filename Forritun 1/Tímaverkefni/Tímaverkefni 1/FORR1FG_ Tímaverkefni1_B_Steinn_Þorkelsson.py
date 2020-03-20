#FORR1FG05AU-Hát - Tímaverkefni 1 - B - Steinn Þorkelsson
import random
number = 0
tilraunir = 1
while number < 1 or number >100:
    number = int(input("Sláðu inn tölu frá 1 - 100 sem að tölvan á að giska á: "))
    if number > 100:
        print ("Talan verð að verða jafn há eða lægri 100!")
    if number < 1:
        print ("Talan verður að vera jafn há eða hærri en 1")
guess = random.randint(1, 100)
print ("Tölvan giskar á töluna", guess)
while guess != number:
    if guess > number:
        guess -= 1
        tilraunir = tilraunir + 1
        guess = random.randint(1, guess)
    elif guess < number:
        guess += 1
        tilraunir = tilraunir + 1
        guess = random.randint(guess, 100)
    print ("Tölvan giskar á töluna", guess)

print(f'Tölvan giskaði {guess} eftir {tilraunir} tilraunir og það var rétt)