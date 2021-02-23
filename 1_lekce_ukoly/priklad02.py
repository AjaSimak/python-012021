sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
soucastky = input("Zadej kód součástky: ")

if soucastky in sklad:
    print ("Součástka je skladem.")
    amount = int(input("Zadej nakupované množství: "))
    pocetSoucastek = sklad.get(soucastky)
    if amount>=pocetSoucastek:
        print (f"Omlouváme se, ale na skladě je pouze {pocetSoucastek} kusů.")
        sklad.pop(soucastky)
        print(f"Můžete si vybrat z těchto jiných součástek {sklad}.")
    else:
        print(f"Na skladě je {pocetSoucastek} kusů, Vámi požadované množství dodáme.")
        pocetSoucastekNovy=int(pocetSoucastek - amount)
        print(f"Nyní na skladě zbývá {pocetSoucastekNovy}.")
else:
    print ("Součástka není skladem.")


