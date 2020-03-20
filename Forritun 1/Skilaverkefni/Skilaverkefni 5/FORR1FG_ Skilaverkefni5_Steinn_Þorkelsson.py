#FORR1FG05AU-Hát - Skilaverkefni 5 - Steinn Þorkelsson
choice = 0
while choice != '4':
    print('1. Liður 1')
    print('2. Liður 2')
    print('3. Liður 3')
    print('4. Hætta í forritinu')
    print()
    choice = input('Veldu Tölu: ')
    if choice == "1":
        val1 = 'J'
        while val1 == 'J':
            ok = False
            while not ok:
                kt = input('Kennitala: ')
                if len(kt) == 10 and int(kt[0:2]) > 0  and int(kt[0:2]) < 32 and int(kt[2:4]) > 0 and int(kt[2:4]) < 13:
                    ok = True
                    print(f"Vel gert þér tókst að skrifa inn rétta kennitölu {kt}")
                    print()
                else:
                    print('Kennnitalan er vitlaus slegin inn')
                    print()
                val1 = input('Endurtaka?[J/N]').upper()
    if choice == "2":
        val2 = 'J'
        while val2 == 'J':
            ok = False
            while not ok:
                strengur = input('Sláðu inn streng sem er að minnsta kosti 5 stafir: ')
                if len(strengur) > 4:
                    ok = True
                    lengd = len(strengur)
                    nyrstrengur = strengur[:2] + strengur[lengd-2:]
                    print(nyrstrengur)
                    print(nyrstrengur.lower())
                    print(nyrstrengur.upper())
                    print(nyrstrengur)
                    print()
                else:
                    print('Strengurinn verður að vera minnst fimm stafir.')
                val2 = input('Endurtaka?[J/N]').upper()

    if choice == "3":
        val3 = 'J'
        while val3 == 'J':
            nafn = input('Sláðu inn nafn: ')
            print(nafn)
            while len(nafn) > 0:
                nafn = nafn[1:]
                print(nafn)
            val3 = input('Endurtaka?[J/N]').upper()
    if choice == "4":
        print('Bæ')
        break

