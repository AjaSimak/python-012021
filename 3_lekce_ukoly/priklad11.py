class Auto:
  def __init__(self, registracni_znacka, znacka_typ, pocet_km):
    self.registracni_znacka = registracni_znacka
    self.znacka_typ = znacka_typ
    self.pocet_km = pocet_km
    self.dostupnost = True

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)