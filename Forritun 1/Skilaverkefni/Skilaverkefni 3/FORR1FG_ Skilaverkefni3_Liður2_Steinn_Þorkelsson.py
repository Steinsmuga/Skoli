#FORR1FG05AU-Hát - Skilaverkefni 3 - Liður2 - Steinn Þorkelsson

print('Reiknum út flatarmal á ferhyrningi')
lengd = float(input('Sláðu inn lengdina: '))
breidd = float(input('Sláðu inn breiddina: '))
print('Flátarmálið er:', breidd *lengd, "cm2")
svar = input('Má bjóða þér að endturtaka?: [J/N] ').upper()
while svar == "J":
    lengd = float(input('Sláðu inn lengdina: '))
    breidd = float(input('Sláðu inn breiddina: '))
    svar = input('Má bjóða þér að endturtaka?: [J/N] ').upper()
    if svar == "N":
        break