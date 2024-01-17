# syntax van een functie in python
def zeg_hallo():
    print("Hallo, wereld!")
zeg_hallo()

# voorbeeld van indentatie binnen een functie
def beslissing_maken():
    antwoord = input("Wil je iets doen?: ")

    if antwoord.lower() == "ja":
        print("Joepie!")
    else:
        print("Oké, misschien later.")

beslissing_maken()

# dit genereert een foutmelding
def voeg_strings_samen(tekst1, tekst2):
resultaat = tekst1 + tekst2
print(resultaat)

z = voeg_strings_samen("hallo", "wereld")

# return values
def bereken_omtrek(breedte, hoogte):
    omtrek = 2 * (breedte + hoogte)
    return omtrek

omtrek_1 = bereken_omtrek(5, 3) # We slaan het resultaat van de functie op in een variabele
omtrek_2 = bereken_omtrek(4, 2)
som_omtrekken = omtrek_1 + omtrek_2

print("De som van de omtrekken is:", som_omtrekken)

# nieuwe lijn
print("Dit is de eerste regel.\nDit is de tweede regel.")