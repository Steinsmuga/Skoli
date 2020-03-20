#FORR1FG05AU-Hát - Skilaverkefni 4 - Steinn Þorkelsson
choice = 0
while choice != "6":
    print('1. Liður 1')
    print('2. Liður 2')
    print('3. Liður 3')
    print('4. Liður 4')
    print()
    choice = input('Veldu tölu: ')
    if choice == "1":
        val1 = 'J'
        while val1 == 'J':
            heiltala = int(input('Sláðu inn heiltölu: '))
            if (heiltala % 5 == 0) and (heiltala >=5) and (heiltala <= 45):
                print(f'{heiltala} er í fimmm sinnum töflunni')
            else:
                print(f'{heiltala} er ekki í fimm sinnum töflunni')
            val1 = input('Endurtaka?[J/N]').upper()
    elif choice == "2":

        val2 = 'J'
        while val2 == 'J':
            artal = int(input('Sláðu inn ártal: '))
            hlaupar = False
            if (artal % 4 == 0):
                if (artal % 100) == 0:
                    if (artal % 400) == 0:
                        hlaupar = True
                else:
                    hlaupar = True
                print(f'Árið {artal} er hlaupár')
            else:
                print(f'Árið {artal} er ekki hlaupár')
            val2 = input('Endurtaka?[J/N]').upper()

    elif choice == '3':
        val3 = 'J'
        while val3 == 'J':
            summa = 1
            numer = int(input('Sláðu inn heiltölu: '))
            for i in range(1, numer + 1):
                summa = summa*i
            print(summa)
            val3 = input('Endurtaka?[J/N]').upper()
    elif choice == '4':
        val4 = 'J'
        while val4 == 'J':

            gridtala = int(input('Sláðu inn tölu frá 1-9: '))
            if 0 < gridtala <10:
                for x in range(1, gridtala + 1):
                    print('*' * x)
                val4 = input('Endurtaka?[J/N]').upper()
    else:
        print('Bæ')
        break






