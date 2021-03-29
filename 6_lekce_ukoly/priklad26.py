#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
platy_2021_02 = pandas.read_csv("platy_2021_02.csv")

zam_praha["mesto"] = "Praha"
zam_plzen["mesto"] = "Plzen"
zam_liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
platy_zamestnancu = pandas.merge(zamestnanci, platy_2021_02, how = "left", on="cislo_zamestnance")
nepracujici = platy_zamestnancu[platy_zamestnancu["plat"].isnull()]
nepracujici.to_csv("nepracujici.csv", index=False)

prumer_plat = platy_zamestnancu.groupby("mesto")["plat"].mean()
zamestnanci.to_csv("zamestnanci.csv", index=False)

print(platy_zamestnancu.head())
print(zamestnanci.shape)
print(platy_zamestnancu.shape)
print(nepracujici)
print(prumer_plat)