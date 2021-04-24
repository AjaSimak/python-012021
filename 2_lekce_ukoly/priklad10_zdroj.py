def zakazky(odvetvi, obrat, zeme, konference=False, newsletter=False):
  if odvetvi == odvetvi["automotiv"]:
    body = 3
  elif odvetvi == odvetvi["retail"]:
    body = 2
  else:
    body = 0
  return body

odvetvi = input("Ve kterém odvětví podniká firma: ")

  if obrat < 10:
    body = 0
  elif obrat > 1000:
    body = 1
  else:
    body = 3
  return body

obrat = input("Jaký je obrat firmy v mil. EUR: ")

  if zeme == "Česko":
    body = 2
  elif zeme == "Slovensko":
    body = 2
  elif zeme == "Německo, Francie":
    body = 1
  else:
    body = 0
  return body

zeme = input("Z jaké země firma pochází: ")

  if konference == True:
    body = 1
  return body
konference = input("Byl zákazník na konferenci: (True/False)")

  if newsletter == True:
    body = 1
  return body
newsletter = input("Odebírá zákazník newsletter: (True/False)")

total += body
print(zakazky(body))

  if total < 5:
    print(f"Šance je malá.")
  elif total > 8:
    print(f"Šance je vysoká.")
  else:
    print (f"Šance je střední.")

