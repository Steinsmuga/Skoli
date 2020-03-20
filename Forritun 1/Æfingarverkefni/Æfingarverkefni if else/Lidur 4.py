"""# Lidur4: MargfaldaFasta
Forritið spyr notanda um tölu á bilinu 0 - 25.
Forritið margfaldar síðan innslegna tölu með 1,7 og birtir niðurstöðuna.
Ef sleginn er inn tala sem er 0 eða minni eða 25 og hærri á að skrifa “Rangur innsláttur”.
"""
tala = int(input('Sláðu inn tölu á bilinu 0 - 25: '))
if tala > 0 and tala < 25:
    print(tala, "sinnum 1.7 er:",tala * 1.7)
else:
    print('Rangur innsláttur')