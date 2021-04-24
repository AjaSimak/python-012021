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
    radek.pop("Jméno")
    prumer_znamek = int(sum(radek.values())/len(radek))

      if prumer_znamek < 1.5:
        return "Prospěl s vyznamenáním"
      elif radek.values() == 5:
        return "Neprospěl"
      else:
        return "Prospěl"

print(ohodnot_studenta())