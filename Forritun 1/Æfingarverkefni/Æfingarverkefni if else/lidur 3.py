"""Forritið spyr notanda um aldur.
Forritið á að bregðast mismunandi við eftir því hvaða tala er sleginn inn.
Ef slegin er inn tala á bilinu:
0‐6  	Þá á að birta textann “Nú, svo þú ferð að byrja í skóla“
7‐15 	Þá spyr forritið hvort viðkomandi ætli í menntaskóla og bregst við á
mismunandi hátt eftir því hvort svarað er með J eða N.
16‐105  Þá kveður forritið og segir „Gangi þér vel í framtíðinni“
annars 	 Svarar forritið:  þú hefur svarað spurningunni vitlaust
"""
aldur = int(input("Hvað ertu gamall?"))
if aldur < 0 or aldur > 105:
    print('þú hefur svarað spurningunni vitlaust')
elif aldur > 6 and aldur < 16:#in [7,8,9,10,11,12,13,14,15]:
    menntaskoli =  input('Ætlar þú í menntaskóla?(J eða N): ').upper()
    if menntaskoli == 'J':
        print('Flott hjá þér!!!')
    elif menntaskoli == 'N':
        print('Gangi þér vel með það...')
elif aldur >15:
    print('Gangi þér vel í framtíðinni <3')
