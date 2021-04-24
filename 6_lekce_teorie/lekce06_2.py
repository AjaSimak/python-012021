#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")

import pandas

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
studenti = pandas.read_csv("studenti.csv")
predsedajici = pandas.read_csv("predsedajici.csv")
predsedajici["den"] = predsedajici["den"].str.strip()
#funkce strip - zbaví mezer na začátku a na konci - u predsedajícího byla za pondělím mezera


vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")

vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on=["den"])
#print(vysledky_se_jmeny_a_predsedajicimi.head()) -> je prázdný, protože sloupec "jméno" jsou v souborech odlišné
#pandas propojuje tabulky podle sloupců, které se stejně jmenují
#použít funkci "on" - propojí pomocí vybraného sloupce

print(vysledky_se_jmeny_a_predsedajicimi)




