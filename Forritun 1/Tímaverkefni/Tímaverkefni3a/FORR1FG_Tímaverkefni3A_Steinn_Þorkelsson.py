#FORR1FG05AU-Hát - Tímaverkefni3a - Steinn Þorkelsson
import datetime
import re
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
        listi = []
        fleiri = 'J'
        while fleiri == 'J':
            ok = False
            while not ok:
                password = input('Sláðu inn lykilorð: ')
                upper = 0
                lower = 0
                digit = 0
                for c in password:
                    if c.isupper():
                        upper += 1
                    elif c.islower():
                        lower += 1
                    elif c.isdigit():
                        digit += 1
                if lower == 0:
                    print('Lykilorð verður að innihalda a. m. k. einn lágstaf!')
                elif upper == 0:
                    print('Lykilorð verður að innihalda a. m. k. einn hástaf!')
                elif digit == 0:
                    print('Lykilorð verður að innihalda a. m. k. einn tölustaf!')
                elif len(password) < 8:
                    print('Lykilorð verður að vera minnst 8 stafir!')
                elif password in listi:
                    print('Lykilorð hefur verið notað áður!')
                else:
                    listi.append(password)
                    ok = True
                    print(f"{password} er fínt lykilorð")
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

