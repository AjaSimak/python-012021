sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total = 0
for key, value in sales.items():
    print(f"Knihy {key} se prodalo {value} kusů.")
    total += value
#total = total + value#
#items - pracuji s dvojicí#
#sales.items -> vrací obojí - i klíč i hodnota, nebo lze sales.values, když chci jen hodnotu#
print(f"Celkem bylo prodáno {total} knih.")

books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for items in books:
    if items["year"] == 2019:
        total += items["sold"] * items["price"]
print(f"Celkové tržby jsou {total}.")
#násobí se první, program pozná, co má dělat dřív za matematické operace#
#počítám tržby jen pro rok 2019#
#mezi for a in je proměnná, je jedno, jak se jmenuje#
#ale key a value je daná pořadím - i kdybych napsala value, pak key, tak stejně bude na prvním místě ten klíč#

#projít si čtení na doma v lekci slovníky a cykly#

#FUNKCE#

def greetUser():
  print("Ahoj")
greetUser()
#kdyby greetUser byla odszená o 2, tak nedojde k zavolání - > rekurze (volá sama sebe)#
#bez zavolání greetUser, tak se nezobrazí, on pozná, že tam funkce je, ale nezavolá ji sám#
# do () se dává vstup - parametr - ale např. "name" je jen uvnitř jen funkce, můžu s ní pracovat i jinde, nebude souviset#


def greetUser(name):
  print(f"Ahoj {name}!")
greetUser("Ajo")
#ale nemůžou tam být 2 jména, např. "Ajo", "Pythone"#

def sumTwoNumbers(a, b):
  return a + b
result = sumTwoNumbers(5, 9)
print(result)
#result je pomocná proměnná, je to pak přehlednější#
#pass - když chci po : si napsat něco na později, aby mi to ted fungovalo#

def getMark(points):
  if points <= 60:
    mark = 5
  elif points <= 70:
    mark = 4
  elif points <= 80:
    mark = 3
  elif points <= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Zadej počet bodů: ")
points = int(points)
mark = getMark(points)
if mark == 5:
  points = input("Počet bodů v opravném testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")


#rozšíření o bonus#
def getMark(points, bonus=0):
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
print(f"Výsledná známka je {mark}.")
#ten, kdo píše opravný test, tak už se mu nezapočítávají bonusové body#
