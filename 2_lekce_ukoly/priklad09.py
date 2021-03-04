vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]
jmeno = {}
def ohodnot_studenta(jmeno):
  for radek in vysledky:
    if radek["Jméno"] == jmeno:
      znamky = radek.values()
      soucet_znamek = int(sum(znamky))
      return soucet_znamek // len(radek[1:4])

    """if prumer_znamek < 1.5 and znamky < 3:
          return f"Prospěl s vyznamenáním"
    elif predmety < 5:
      return f"Neprospěl"
    else:
      return f"Prospěl" """

jmeno = input("Zadej jméno studenta: ")
print(ohodnot_studenta(jmeno))

#cyklus by měl jít po jednotlivých řádcích. dle jména studenta
#poté sečíst předměty
#https://www.geeksforgeeks.org/python-program-to-find-the-sum-of-all-items-in-a-dictionary/
#https://www.kite.com/python/answers/how-to-sum-the-values-in-a-dictionary-in-python
