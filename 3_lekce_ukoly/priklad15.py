from datetime import datetime

datum = input("Zadej datum návštěvy kina (den.měsíc.rok): ")
zacatek_drazsi = datetime.strptime("1.7.2021", "%d.%m.%Y")
konec_drazsi = datetime.strptime("10.8.2021", "%d.%m.%Y")
zacatek_levnejsi = datetime.strptime("11.8.2021", "%d.%m.%Y")
konec_levnejsi = datetime.strptime("31.8.2021", "%d.%m.%Y")
datum = datetime.strptime(datum, "%d.%m.%Y")

if datum >= zacatek_drazsi and datum <= konec_drazsi:
  pocet_listku = int(input("Zadej počet lístků: "))
  cena = pocet_listku * 250
  print(cena)
elif datum >= zacatek_levnejsi and datum <= konec_levnejsi:
  pocet_listku = int(input("Zadej počet lístků: "))
  cena = pocet_listku * 180
  print(cena)
else:
  print("Kino nehraje.")