#FORR1FG05AU-Hát - Tímaverkefni 2 - Steinn Þorkelsson
import random
choice = 0
while choice != '4':
    print()
    print('1. Liður 1')
    print('2. Liður 2')
    print('3. Liður 3')
    print('4. Hætta í forritinu')
    print()
    choice = input('Veldu Tölu: ')
    if choice == "1":
        hundrad = int(input('Sláðu inn tölu minni en hundrað: '))
        print(f"Nú er talan {hundrad}")
        summa = 0
        while hundrad < 100:
            summa += hundrad
            hundrad += 1

            print(f"Nú er talan {hundrad}")
        print(f"Samtals {summa + 100}")
    if choice == "2":
        tala1 = int(input("Sláðu inn tölu: "))
        tala2 = int(input(f"Sláðu inn aðra tölu hærri en {tala1}: "))
        for fjorir in range(tala1, tala2 + 1, 4):
            print(fjorir,'=>', end=' ')
    if choice == "3":
        #tala = int(input("Sláðu inn tölu á bilinu 1 til 1000: "))
        tala = random.randint(1,1000)
        if tala < 501:
            while tala > 0:
                print(tala, ' ', end='')
                tala = tala - 1
        else:
            for plus in range(tala,1001,1):
                print(plus, ' ',end='')





