class Auto:
  def __init__(self, registracni_znacka, znacka_typ, tachometr):
    self.registracni_znacka = registracni_znacka
    self.znacka_typ = znacka_typ
    self.tachometr = tachometr
    self.dostupnost = True

  def vrat_auto(self, pocet_km, pocet_dni):
    self.pocet_dni = int(pocet_dni)
    self.pocet_km = int(pocet_km)
    self.tachometr += int(pocet_km)

    if self.pocet_dni < 7:
      price = 400 * self.pocet_dni
    else:
      price = 300 * self.pocet_dni
    return f"Cena za výpůjčku je {price} Kč s {self.tachometr} km, vozidlo je nyní volné."

pegueot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

auta = {
  "Pegueot": pegueot,
  "Škoda": skoda
}

vypujcka = input("Jakou značku si přejete vrátit? (Pegueot/Škoda)")
pocet_km = input("Kolik kilometrů jsi ujel? ")
pocet_dni = input("Kolik dní jste měli auto půjčené? ")

print(auta[vypujcka].vrat_auto(pocet_km, pocet_dni))


