#FORR1FG05AU-Hát - Tímaverkefni3a - Steinn Þorkelsson
import datetime
choice = 0
while choice != "6":
    print('1. Liður 1')
    print('2. Liður 2')
    print('3. Liður 3')
    print('4. Liður 4')
    print('5. Liður 5')
    print('6. Hætta')
    choice = input('Veldu Tölu: ')

    if choice == "1":
        lykilord = input("Sláðu inn sterkt lykilorð sem er að minnsta kosti: \n 8 stafir að lengd \n inniheldur að minnsta kosti: \n eina tölu, einn stóran staf og einn lítinn staf: ")

        listi =[]
        uppercase = 0
        lowercase = 0
        number = 0
        fleiri = 'J'

        while fleiri == 'J':
            ok = False
            while not ok:
                lykilord = input("Sláðu inn sterkt lykilorð sem er að minnsta kosti: \n 8 stafir að lengd \n inniheldur að minnsta kosti: \n eina tölu, einn stóran staf og einn lítinn staf: ")
                for i in lykilord:
                    if i.isupper():
                        uppercase += 1
                    elif i.islower():
                        lowercase += 1
                    elif i.isdigit():
                        number += 1
                    elif len(lykilord) < 8:
                        print(f"{lykilord} er ekki nógu gott")
                    elif uppercase > 0 and lowercase > 0 and number > 0:
                        print(f"{lykilord} er gott lykilorð")
                    else:
                        print(f"{lykilord} er ekki nógu gott")
                if lykilord not in listi:
                    listi.append(lykilord)
                    ok = True
                else:
                    print(f"{lykilord} hefur nú þegar verið notað")
                fleiri = input('Fleiri? [J/N]').upper()

    elif choice == "2":
        today = datetime.date.today()
        print("Í dag er",today.strftime(" %d-%b-%Y"))

    elif choice == "3":
        strengur = 'This is another sample string'
        print(strengur)
        nytt_ord = strengur.strip().split()[-2]
        print(nytt_ord)

    elif choice == "4":
        credit_str = "xxxx----xxxx-8888------xxxx"

        new_credit_str = credit_str[credit_str.index('8'):credit_str.index('8') + len('8888')]

        print(new_credit_str)
    elif choice == "5":
        breyta = input("Sláðu inn orð: ")
        print(breyta[-1:] + breyta[1:-1] + breyta[:1])

    else:
        print("bæ :( ")
listi = []
fleiri = 'J'
while fleiri == 'J':
    ok = False
    while not ok:
        password = input('Sláðu inn lykilorð:')
        if not password in listi:
            listi.append(password)
            ok = True
        else:
            print('Lykilorð hefur verið notað áður!')
    fleiri = input('Fleiri? [J/N]').upper()


