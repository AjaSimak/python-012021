class Auto:
  def __init__(self, registracni_znacka, znacka_typ, pocet_km):
    self.registracni_znacka = registracni_znacka
    self.znacka_typ = znacka_typ
    self.pocet_km = pocet_km
    self.dostupnost = True

  def pujc_auto(self):
    if self.dostupnost:
      self.dostupnost = False
      return "potvrzuji zapůjčení vozidla"
    return "vozidlo není k dispozici"

  def get_info(self):
      msg = f"Registrační značka: {self.registracni_znacka} a typ vozidla: {self.znacka_typ}"
      return f"{msg}"

pegueot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

auta = {
  "Pegueot": pegueot,
  "Škoda": skoda
}

vypujcka = input("Jakou značku si přejete půjčit? (Pegueot/Škoda)")
print(auta[vypujcka].get_info())
print(auta[vypujcka].pujc_auto())
vypujcka = input("Jakou značku si přejete půjčit? (Pegueot/Škoda)")
print(auta[vypujcka].get_info())
print(auta[vypujcka].pujc_auto())
vypujcka = input("Jakou značku si přejete půjčit? (Pegueot/Škoda)")
print(auta[vypujcka].get_info())
print(auta[vypujcka].pujc_auto())
vypujcka = input("Jakou značku si přejete půjčit? (Pegueot/Škoda)")
print(auta[vypujcka].get_info())
print(auta[vypujcka].pujc_auto())

