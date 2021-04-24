def zakazky(odvetvi):
  if odvetvi == "automotiv":
    body = 3
  elif odvetvi == "retail":
    body = 2
  else:
    body = 0
  return body
odvetvi = input("Jaké odvětví? ")
body = zakazky(odvetvi)

print(f"Celkem bodů {body}")


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