class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

class Uzivatel:
  def __init__(self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0

  def pripocti_zhlednuti(self, delka_sledovani):
    self.delka_sledovani = delka_sledovani

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_celkova_delka(self):
    return self.delka


class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def get_celkova_delka(self):
    self.delka_serialu = self.delka_epizody * self.pocet_epizod
    return self.delka_serialu

film = Film("Ohni se mnou pojď", "mystery", 120)
serial = Serial("Twin Peaks", "mystery", 30, 90)
uzivatel = Uzivatel("Andrea")


uzivatel.pripocti_zhlednuti(serial.get_celkova_delka()+film.get_celkova_delka())
print(uzivatel.delka_sledovani)