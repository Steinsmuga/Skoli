#FORR1FG05AU-Hát-Verkefni2-liður1-Steinn Þorkelsson
print("Sláðu inn 3 tölur")
tala1=int(input("Tala 1: "))
tala2=int(input("Tala 2: "))
tala3=int(input("Tala 3: "))
if tala1>tala2:
    if tala1<tala3:
        median= tala1
    elif tala2>tala3:
        median= tala2
    else:
        median= tala3
else:
    if tala1>tala3:
        median= tala1
    elif tala2<tala3:
        median= tala2
    else:
        median= tala3
print("Talan í miðjunni er:",median)