#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

print(staty[["population", "area"]])
#když dám 2 proměnné, tak jsou 2 závorky - dělám totiž ještě z toho seznam

populace = staty["population"]
#vybírám jeden sloupec, tedy jeden rozměr, je to série, není to dataframe

#když chci sečíst celou populaci, vypisuje to jako číslo
print(populace.sum())

print(staty["population"] < 1000)
#vypíše všechny státy a u toho True nebo False, jestli byla splněná podmínka
#pokud chci vypsat konkrétní státy, tak když uvidí False, tak dá pryč, pokud True, tak tam řádek nechá
# => musím to obalit do dalšího dotazu
print(staty[staty["population"] < 1000])

pidistaty = staty[staty["population"] < 1000]
print(pidistaty[["area", "population"]])

#lidnaté EV státy a podmínky (EV a víc jak 20 mil. ob), každý dotaz musí mít svou vlastní ()
# | (alt + w) je nebo; & je a zároveň
lidnate_evropske_staty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
print(lidnate_evropske_staty)
print(lidnate_evropske_staty["population"])

vyznamne_staty = staty[(staty["population"] > 1_000_000_000) | (staty["area"] > 3_000_000)]
print(vyznamne_staty)

#podmínka na seznam regionů
zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]
print(zap_vych_evropa)







