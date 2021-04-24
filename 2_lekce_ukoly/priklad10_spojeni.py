def zakazky(odvetvi, obrat):
  if odvetvi == "automotiv":
    body1 = 3
  elif odvetvi == "retail":
    body1= 2
  else:
    body1 = 0
  if obrat < 10:
    body2 = 0
  elif obrat > 1000:
    body2 = 1
  else:
    body2 = 3
  return body1 + body2

odvetvi = input("Jaké odvětví? ")
obrat = input("Jaký je obrat firmy v mil. EUR: ")
obrat = int(obrat)
#soucet_bodu += body
#body = zakazky(odvetvi, obrat)
print(zakazky(odvetvi, obrat))
#print(f"Celkem bodů {body}")

"""def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Zadej počet bodů: ")
points = int(points)
bonus = input("Zadej počet bonusových bodů: ")
bonus = int(bonus)
mark = getMark(points, bonus)
mark = getMark(points)
if mark == 5:
  points = input("Počet bodů v opravném testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")"""
