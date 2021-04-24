#import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")


#počítání sloupců

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

staty["population_density"] = staty["population"] / staty["area"]
#print(staty.head())

#řazení (může se dát by=) staty.sort_values(by="population")
#defaultně je vzestupně
staty = staty.sort_values("population_density")
print(staty.head())

#sestupně
#napíšu, že vzestupně = false
staty = staty.sort_values("population_density", ascending=False)
print(staty.head())

#řazení podle více sloupců
# pomocí by