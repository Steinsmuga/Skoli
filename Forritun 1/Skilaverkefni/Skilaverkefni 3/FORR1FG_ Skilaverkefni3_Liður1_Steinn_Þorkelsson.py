#FORR1FG05AU-Hát - Skilaverkefni 3 - Liður 1 - Steinn Þorkelsson

tala = int(input('Sláðu inn heiltölu: '))
print("Þú hefur valið töluna", tala)
svar = input('Má bjóða þér að velja aðra tölu?: [J/N]').upper()
while svar == "J":
    tala = int(input('Sláðu inn heiltölu: '))
    print("Þú hefur valið töluna", tala)
    svar = input('Má bjóða þér að velja aðra tölu?: [J/N]').upper()
    if svar == "N":
        break