"""
subregiony = {}
nazevRegionu = input("Napiš název regionu: ")
sumSubRegion = 0
for nazevRegionu in staty:
  subregion = nazevRegionu["subregion"]
  populace = nazevRegionu["population"]
  if nazevRegionu in subregiony.items():
    sumSubRegion[subregion] += populace
      for subregion, populace in subregiony.items():
        totalSubregion += sumSubRegion
        print(f" {subregion} čítá {totalSubregion} obyvatel.")
  else:
    sumSubRegion = populace
  print(nazevRegionu["subregion"], sumSubRegion)
 #sumSubRegion += nazevRegionu['population']
 # print(f"V subregionu {nazevRegionu['subregion']} žije {sumSubRegion}.")#
subregiony = {}
totalSubregion = 0
subregion = nazevRegionu["subregion"]
populace = nazevRegionu["population"]
region = nazevRegionu["region"]
for nazevRegionu in staty:
  for subregion, populace in subregiony.items():
    totalSubregion += sumSubRegion
    print(f" {subregion} čítá {totalSubregion} obyvatel.")

  #jenže to se mi navyšuje postupně - potřebuji celý součet# """

totalSubregion = 0
for nazevRegionu in staty:
  if nazevRegionu["region"] == Europe:
    totalSubregion += nazevRegionu["population"]
print(totalSubregion, nazevRegionu["region"])

#příklad z konzultace#
"""for stat in staty:
  print(stat["subregion"])

subregiony = {}
for stat in staty:
  subregion[stat["subregion"]] = stat["area"]"""

#vytvoř si proměnnou, která se uloží do nového slovníku#
#čtení na doma ->podle toho to jde udělat#