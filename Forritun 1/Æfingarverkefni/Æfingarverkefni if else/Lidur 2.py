"""Forritið spyr notanda um nafn mánaðar.
Forritið skrifar síðan út númer hvað mánuðurinn er.
Ef slegið er inn nafn mánaðar sem er ekki til  á að skrifa “‘Eg þekki ekki þennan mánuð”."""

month = input("Sláðu inn nafn á mánuði:")

if month == 'janúar':
    print("Mánuðurinn er nr. 1")
if month == 'febrúar':
        print("Mánuðurinn er nr. 2")
if month == 'mars':
        print("Mánuðurinn er nr. 3")
if month == 'apríl':
        print("Mánuðurinn er nr. 4")
if month == 'maí':
        print("Mánuðurinn er nr. 5")
if month == 'júní':
        print("Mánuðurinn er nr. 6")
if month == 'júlí':
        print("Mánuðurinn er nr. 7")
if month == 'ágúst':
        print("Mánuðurinn er nr. 8")
if month == 'september':
        print("Mánuðurinn er nr. 9")
if month == 'október':
        print("Mánuðurinn er nr. 10")
if month == 'nóvember':
        print("Mánuðurinn er nr. 11")
if month == 'desember':
        print("Mánuðurinn er nr. 12")
else:
        print('Eg þekki ekki þennan mánuð')