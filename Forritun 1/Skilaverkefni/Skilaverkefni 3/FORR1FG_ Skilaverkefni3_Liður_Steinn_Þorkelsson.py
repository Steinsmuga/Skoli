"""Skrifaðu forritskóða sem biður um upphæð í krónum ef upphæðin er yfir 10.000 kr.
prentast út allar tölur frá 1 og upp að upphæðinni sem slegin var inn.
 Ef upphæðin er undir 10.000 kr.
 Prentast út allar tölur frá upphæðinni sem slegin var inn og niður að 1(öfug röð).
Ef upphæðin er 10.000 kr. Prentast út „10.000 kr.“ 10000 sinnum og allt í einni línu."""
kronur = int(input('Sláðu inn upphæð í krónum: '))
teljari = 1
while kronur < 10000:
  print(teljari + 1)
  if teljari == kronur:
      break
  teljari = teljari + 1
if kronur == 10000:
    print('10000 '  * 10000)
