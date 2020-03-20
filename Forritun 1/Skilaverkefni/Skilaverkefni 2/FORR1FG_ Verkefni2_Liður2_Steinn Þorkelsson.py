#FORR1FG05AU-Hát-Verkefni2-liður2-Steinn Þorkelsson
val = input(str("Veldu tommur eða cm(T eða C): "))
number = float(input("Sláðu inn tölu: "))
if val in "Cc":
    print(number , "CM eru" , number/2.54,"Tommur")
else:
    print(number ,"tommur eru", number*2.54, "Cm")