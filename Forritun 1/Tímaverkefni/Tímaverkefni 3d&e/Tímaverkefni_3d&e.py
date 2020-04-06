from random import randint
ordalisti = ['kartafla', 'epli', 'appelsína', 'banani', 'jarðaber']
ord = ordalisti[randint(0,4)]
#print(ord)
fjoldi_stafa = len(ord)
gisk = []
notadir_stafir = []
for i in range(fjoldi_stafa):
    gisk.append('_')
for c in gisk:
    print(c, end=' ')
print()

tilraunir = 0
rettir = 0
while rettir < fjoldi_stafa and tilraunir < 10:
    stafur = input('Stafur: ').lower()
    if stafur not in notadir_stafir:
        notadir_stafir.append(stafur)
        for i in range(fjoldi_stafa):
            if ord[i] == stafur:
                gisk[i] = stafur
                rettir += 1
        tilraunir += 1
        for c in gisk:
            print(c, end=' ')
        print()
    else:
        print('Búið að nota stafinn ', stafur)

print('Tilraunir: ', tilraunir, ' réttir', rettir)