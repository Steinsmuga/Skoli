#FORR1FG05AU-Hát - Skilaverkefni 3 - Liður 5 - Steinn Þorkelsson

print('halló')
teljari = 1
val = [1,2,3]
while val != '3':
    print('1. Biður um 10 tölur. Finnur  summu þeirra og meðaltal.')
    print('2. Biður um tölu og athugar hvort talan sé jöfntala eða oddatala ')
    print('3. Hætta í forritinu og skrifa ’Ég er frábær forritari’ á skjáinn 10 sinnum og tilgreina hversu oft forritið var keyrt. ')
    val = int(input('Hvað er valið?: '))
    print('Þú hefur valið:', val)
    if val == 1:
        print(' Sláðu inn 10 tölur hér fyrir neðan:')
        teljari = teljari + 1
        tala1 = int(input('Tala 1: '))
        tala2 = int(input('Tala 2: '))
        tala3 = int(input('Tala 3: '))
        tala4 = int(input('Tala 4: '))
        tala5 = int(input('Tala 5: '))
        tala6 = int(input('Tala 6: '))
        tala7 = int(input('Tala 7: '))
        tala8 = int(input('Tala 8: '))
        tala9 = int(input('Tala 9: '))
        tala10 = int(input('Tala 10: '))
        summa = tala1 + tala3 + tala4 + tala5 + tala6 + tala7 + tala8 + tala9 + tala10
        medaltal = round(summa / 10.0)
        print(f'Summa talnanna er {summa} og meðaltalið er {medaltal}')
    if val == 2:
        tala = int(input('Sláðu inn tölu: '))
        teljari = teljari + 1
        if (tala % 2) == 0:
            print(tala,'er jöfntala')
        else:
            print(tala,'er oddatala')
    if val == 3:
        print('Ég er frábær forritari.' * 10 )
        print(f'Forritið var keyrt {teljari} sinnum')
        break

