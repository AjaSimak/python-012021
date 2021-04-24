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
    self.zapis_z_pohovoru = ""

  def uloz_zapis(self, zapis):
    self.zapis = zapis
    #datum_dnes = now.strftime
    if datum_dnes > datum_pohovoru:
      return "Zápis je uložen."
    else:
      return "Pohovor ještě neproběhl."

# Tvým úkolem je předělat funkci (uloz_zapis) a by to fungovalo.

datum_pohovoru= datetime(2020, 10, 25)
#datum_pohovoru_NOK = datetime(2022, 10, 25)

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru)
print(uchazec.uloz_zapis())

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru_NOK)
print(uchazec.uloz_zapis())



#uchazec = Uchazec("Andrea", "andrea@seznam.cz", "25.4.2020")
#print(uchazec.uloz_zapis())

#("%d.%m.%Y")

#https://kodim.cz/czechitas/progr2-python/python-pro-data-1/datum

