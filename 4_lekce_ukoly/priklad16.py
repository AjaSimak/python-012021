class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

  def get_info(self):
    return f"Název je {self.nazev} a žánr je {self.zanr}, "

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

  def get_info(self):
    return super().get_info() + f" film je dlouhý {self.delka} minut."

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody

  def get_info(self):
    return super().get_info() + f" seriál je dlouhý {self.delka_epizody} minut a má {self.pocet_epizod} epizod."

film = Film("Ohni se mnou pojď", "mystery", 120)
serial = Serial("Twin Peaks", "mystery", 30, 90)

print(film.get_info())
print(serial.get_info())

#Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
#Funkce u třídy Polozka vypíše název a žánr.
#Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.