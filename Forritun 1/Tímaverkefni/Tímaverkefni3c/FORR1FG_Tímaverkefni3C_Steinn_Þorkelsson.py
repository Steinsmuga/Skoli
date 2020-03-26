#FORR1FG05AU-Hát - Tímaverkefni3C - Steinn Þorkelsson
import random
import re
'''
Val 1
Forritið framkvæmir eftirfarandi aðgerðir.
•	Skrifar út á skjáinn allar tölur frá 200 til 400 í eina línu. Notið for-lykkju.

Hint:
listi = [1,2,3]
for i in listi:
    print(i, end=' ')

Val 2
Forritið setur 100 tilviljanakenndar (random) tölur á bilinu 2000 til 2030 í lista og framkvæmir eftirfarandi aðgerðir.

•	Birtir meðaltal talnanna með einum aukastaf (round).
•	Finnur og birtir hve oft talan 2005 kom fyrir.
•	Setur allar tölur yfir 2020 sem eru í listanum í annan lista.
•	Birtir allar tölur lægri en 2010 í listanum.


Val  3
Forritið biður um texta og framkvæmir eftirfarandi aðgerðir.

•	Skrifar út textann í hástöfum á skjáinn.
•	Finnur hversu oft stafurinn s kemur fyrir textanum og prentar út fjöldann.
•	Skrifar út stafinn a þar sem það kemur fyrir í textanum annars  ?  þar sem önnur tákn/stafir ættu að vera.
Dæmi: Anna borðar banana   verður   A??a ????a? ?a?a?a
'''




choice = 0
while choice != '4':
    print('Valmynd:')

    print("1 - – Skrifa út tölurnar 200-400 í eina línu.")

    print("2 - – Vinna með tilviljanakenndar (random) tölur.")

    print("3 - – Vinna með texta (streng). ")

    print("4 - - Hætta")

    print()

    choice = input("Sláðu inn tölu: ")

    if choice == "1":
        for i in range(200,401):
            print(i, end=' ')

        print()
    elif choice == "2":
        listi = []
        tveirfimm = 0

        for counter in range(100):
            listi.append(random.randint(2000, 2030))
        print(listi)
        print()
        def Medaltal(listi):
            return sum(listi) / len(listi)
        summa = Medaltal(listi)
        medaltal = round(summa, 2)
        print("Medaltalið er:")
        print("%.1f" % medaltal)
        print()

        for i in listi:
            if i == 2005:
                tveirfimm += 1
        print(f"Talan 2005 kemur {tveirfimm} sinnum fyrir")
        print()
        yfir2020 = [i for i in listi if i > 2020]
        print(f"Tölur yfir 2020:")
        print(yfir2020)
        print()

        print("Tölur undir 2010:")
        for x in listi:
            if x < 2010:
                print(x, end=', ')

        print()
    elif choice == "3":
        texti = input("Sláðu inn orð eða texta: ")
        print(f"Textinn í hástöfum: {texti.upper()}")

        sfjoldi = 0
        for s in texti:
            if s == "s":
                sfjoldi += 1
        print(f'Stafurinn "s" kemur {sfjoldi} sinnum fyrir í textanum')
        print()

        print(re.sub('[b-ö]', '?', texti))
    elif choice == "4":

        print("BÆBÆ")

    else:

        print("Sláðu eingungis inn: 1,2,3,4")

