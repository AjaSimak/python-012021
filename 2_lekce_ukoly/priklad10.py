def zakazky(odvetvi, obrat, zeme, konference=False, newsletter=False):
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
  if zeme == "Česko":
    body3 = 2
  elif zeme == "Slovensko":
    body3 = 2
  elif zeme == "Německo":
    body3 = 1
  elif zeme == "Francie":
    body3 = 1
  else:
    body3 = 0
  if konference == "ano":
    body4 = 1
  else:
    body4 = 0
  if newsletter == "ano":
    body5 = 1
  else:
    body5 = 0

  return body1 + body2 + body3 + body4 + body5

odvetvi = input("Jaké odvětví? ")
obrat = input("Jaký je obrat firmy v mil. EUR: ")
obrat = int(obrat)
zeme = input("Z jaké země firma pochází: ")
konference = input("Byl zákazník na konferenci: (ano/ne)")
newsletter = input("Odebírá zákazník newsletter: (ano/ne)")
print(zakazky(odvetvi, obrat, zeme, konference, newsletter))

if zakazky(odvetvi, obrat, zeme, konference, newsletter) <= 5:
  print(f"Šance je malá.")
elif zakazky(odvetvi, obrat, zeme, konference, newsletter) > 8:
  print(f"Šance je vysoká.")
else:
  print(f"Šance je střední.")