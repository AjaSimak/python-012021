from datetime import datetime
now = datetime.today()
datum_dnes = now.strftime("%d.%m.%Y")

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__(self, jmeno, email, datum_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    self.datum_pohovoru = datum_pohovoru.strftime("%d.%m.%Y")
    self.zapis_z_pohovoru = " "

  def uloz_zapis(self):
#    self.zapis = zapis
    datum_dnes = now.strftime("%d.%m.%Y")
    spravne_datum = self.datum_pohovoru - datum_dnes
    if spravne_datum < 0:
      return "Zápis je uložen."
    else:
      return "Pohovor ještě neproběhl."

uchazec = Uchazec("Andrea", "andrea@seznam.cz", "25.4.2020")
print(uchazec.uloz_zapis())


#https://kodim.cz/czechitas/progr2-python/python-pro-data-1/datum

