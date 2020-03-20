"""1. Finnur hversu mörg bil eru í textanum og hversu mörg orð eru í textanum.
2. Skrifar út fyrstu 5 stafina/táknin í strengnum sem sleginn var inn.
3. Spyr notanda hvað eigi að skrifa út marga stafi/tákn í strengum sem sleginn var inn og skrifar þá út.
4. Segir hvað strengurinn er langur sem notandinn sló inn
5. Snýr fyrsta og aftasta orði strengsins við.
6. Setur allan strenginn sem notandinn sló inn í stóra stafi.
7. Setur allan strenginn sem notandi sló inn í litla stafi.
8. Biður um staf og athugar hvort hann komi fyrir í strengnum og skrifar út hversu oft hann kom.
9. Setur @ í nýjan streng fyrir hvert tákn í upphaflega strengnum nema fyrir bil, birtir nýja strenginn.

		Dæmi: ef textinn er hæ hó, þá birtist  @@ @@
0. Hættir í forritinu
"""
setning = input('Sláðu inn setningu, minnst 7 orð: ')
#print(setning)
teljari = 0
for stafur in setning:
    if stafur == ' ':
        teljari = teljari + 1
#1
print(f'Fjöldi bila eru {teljari}. \nFjöldi orða eru {teljari + 1}.')
#2
print(f'Fyrstu 5 stafirnir eru {setning[0:5]}.')
#3
fjoldi = int(input('Fjöldi?: '))
print(setning[0:fjoldi])
#4
print(f'Fjöldi stafa eru {len(setning)}.')
#5
print(setning[3::-1])
#6
print(setning.upper())
#7
print(setning.lower())
#8
stafur = input('Stafur: ').lower()
counter = 0
for s in setning:
    if s.lower() == stafur.lower():
        counter += 1
print(f'{stafur} kom fyrir {counter} sinnum')