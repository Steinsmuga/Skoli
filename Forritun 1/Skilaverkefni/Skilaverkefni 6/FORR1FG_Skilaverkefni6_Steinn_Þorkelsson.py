#FORR1FG05AU-Hát - Skilaverkefni 6 - Steinn Þo
#  rkelsson
import random
choice = 0
while choice != '5':
    print('1. Random tölur')
    print('2. Talnabil')
    print('3. Strengjalisti')
    print('4. Samanburður')
    print('5. Hætta í forritinu')
    print()
    choice = input('Veldu Tölu: ')

    if choice == "1":
        listi = []
        for counter in range(50):
            listi.append(random.randint(5,70))
        print(f" Óraðað {listi}")
        margfeldi = 1
        """for tala in listi:
            margfeldi *= tala
        print(f"Allar tölur margfaldaðar: {margfeldi}")
        print(max(listi))
        print(min(listi))"""
        #eða flóknari leiðin
        max = listi[0]

        for tala in listi:
            if tala > max:
                max = tala
        print(f"Hæsta talan: {max}")
        min = listi[0]
        for tala in listi:
            if tala < min:
                min = tala
        print(f"Lægsta talan: {min}")
        print(f"Raðað: {sorted(listi)}")
    elif choice == "2":

        listi = []
        for tala in range(2000,3200):
            if tala % 7 == 0 and tala % 5 != 0:
                listi.append(tala)
        print(f"7 gengur upp í þessar tölur en ekki 4{listi}")
        samtala = 0
        for tala in listi:
            samtala += tala
        print(samtala)
    elif choice == "3":
        strengur = input('Sláðu inn 10 orð: ')
        listi = strengur.split()
        radad = sorted(listi)
        print(listi)
        print()

        for k in listi:
            if len(k) == 4:
                print(k, ' ', end='er 4 stafir að lengd')

        for i in range(1, len(listi), 2):
            listi[i] = listi[i][::-1]
        print("Annað hvert orð öfugt:")
        print(listi)

        print()
        print("Listinn raðaður:")
        print(sorted(listi))
        print()
        burt = input('Sláðu inn staf, öll orð sem byrja á stafnum munu eyðast: ')
        fjoldi = 0

        for ord in listi[:]:
            if ord.startswith(burt):
                listi.remove(ord)
                fjoldi += 1
        print(f"{fjoldi} orð voru eydd>")
        print(listi)
        print()
    elif choice == "4":
        string1 = input("Sláðu inn 7 orð: ")
        string2 = input("Sláðu inn 6 orð: ")
        listi1 = string1.split()
        listi2 = string2.split()
        print("Þessi orð birtast í báðum listunum:")
        for sam1 in listi1:
            for sam2 in listi2:
                if sam1 == sam2:
                    print(sam1,' ', end='')
    elif choice == "5":
        print('ok bæ')
        print(":'(")







