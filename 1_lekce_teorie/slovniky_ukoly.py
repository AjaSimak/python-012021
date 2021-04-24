vysvedceni = {"cesky jazyk": 2, "matematika": 1, "dějepis": 3}
print(vysvedceni)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100
print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

number = int(input("Zadejte číslo lístku: "))
if number in tombola:
    win = tombola.pop(number)
    print(f"Vyhráváš: {win}.")
else:
    print("Bohužel nevyhráváš nic.")



passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name = input("Jaké je tvé jméno?: ")

"""
Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, 
které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, 
zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. 
Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

"""

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name = input("Zadej jméno: ")
if name in passwords:
  password = input("Zadej heslo: ")
  if password == passwords[name]:
    print("Smíš vstoupit.")
  else:
    password = input("Nesprávné heslo. Zadej heslo znovu: ")
    if password == passwords[name]:
      print("Smíš vstoupit.")
    else:
      print("Neznáš heslo, vstup zakázán.")
else:
  print("Nejsi na seznamu hostů.")
