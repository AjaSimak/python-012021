books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
#Napiš program, který spočte celkový počet stran, které Gustav přečetl.#
#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.#
total = 0
sum_8 = 0
for items in books:
  total += items["pages"]
  if items["rating"] >= 8:
    sum_8 += 1
    print(f"Hodnocení aspoň osm má {items['title']}, celkem {sum_8} knih.")
print(f"Celkem přečetl {total} stran.")

schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}
#Napiš program, který spočte průměrnou známku ze všech předmětů.#

soucet_znamek = 0
for predmet, znamka in schoolReport.items():
  if znamka == 1:
    print(predmet)
  soucet_znamek += znamka
print (soucet_znamek)
print('Průměrná známka:', soucet_znamek // len(schoolReport))



plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for znacka, majitel in plates.items():
  if znacka[1] == 'P':
    print(majitel)
#1 je tam proto, že na druhém místě#
#video od Andy#




purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]

sumPerPerson = {}
for item in purchaseList:
  person = item["person"]
  value = item["value"]
  if person in sumPerPerson:
    sumPerPerson[person] += value
  else:
    sumPerPerson[person] = value
totalValue = 0
for person, value in sumPerPerson.items():
  totalValue += value
  print(f"{person} utratil(a) za společné nákupy {value} Kč.")

averageValue = totalValue / len(sumPerPerson)
print(f"Průměrná hodnota na osobu je {round(averageValue)} Kč.")


#FUNKCE#
def mult(a, b):
  return a * b
result = mult(3, 4)
print(result)
#nebo print(mult(3, 4)#

def totalPrice(persons, breakfast=False):
  pricePerPerson = 850
  if breakfast:
    pricePerPerson += 125
  return pricePerPerson * persons
print(totalPrice(3))
print(totalPrice(3, True))
#false = není tam defaultně -> pak u printu mám true, když ji chci v ceně#

def monthOfBirth(n):
  month = n[2] + n[3]
  #month = n[2:4] -> slicing, krajní hodnota už se nevypíše, takže pokud chci třetí místo, musím napsat 4
  month = int(month)
  month = month % 50
  return month
print(monthOfBirth("8707150069"))

import random
def roulette(rada, sazka):
  n = random.randint(0, 36)
  print(f"Padlo číslo {n}.")

  if n == 0:
    return -sazka
  if n % 3 == 1 and rada == 1:
    return sazka * 2
  if n % 3 == 2 and rada == 2:
    return sazka * 2
  if n % 3 == 0 and rada == 3:
    return sazka * 2
  return -sazka

rada = int(input("Zadej číslo řady: "))
sazka = int(input("Zadej výši sázky: "))
print(roulette(rada, sazka))
