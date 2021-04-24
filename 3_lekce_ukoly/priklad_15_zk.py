from datetime import datetime
def datum(datum):
  if datum >= zacatek_drazsi and datum <= konec_drazsi:
    return True
  elif datum >= zacatek_levnejsi and datum <= konec_levnejsi:
    return False
  else:
    print("Kino nehraje.")

datum = input("Zadej datum návštěvy kina (den.měsíc.rok): ")
zacatek_drazsi = datetime.strptime("1.7.2021", "%d.%m.%Y")
konec_drazsi = datetime.strptime("10.8.2021", "%d.%m.%Y")
zacatek_levnejsi = datetime.strptime("11.8.2021", "%d.%m.%Y")
konec_levnejsi = datetime.strptime("31.8.2021", "%d.%m.%Y")
datum = datetime.strptime(datum, "%d.%m.%Y")

def listek(pocet_listku):
  if datum(datum) == True:
    cena = pocet_listku * 250
    print(cena)
  elif datum(datum) == False:
    cena = pocet_listku * 180
    print(cena)

  pocet_listku = int(input("Zadej počet lístků: "))