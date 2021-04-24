#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

print(staty.head())
print(staty.info())
#pomocí info vidím sloupce

print(staty.index)

#když chci konkrétní stát, tak dám místo čísla řádku jméno státu
print(staty.loc["Czech Republic"])

#když chci vypsat státy od do; iloc a loc se chová jinak - loc mi vypíše i poslední hodnotu
print(staty.loc["Czech Republic": "Dominican Republic"])

# když chci od začátku až pod Dominikán...
print(staty.loc[: "Dominican Republic"])

#když chci od Uzb do konce
print(staty.loc["Uzbekistan":])

# když dva konkrétní a konkrétní sloupec - pozor na hranaté závorky
print(staty.loc[["Czech Republic", "Slovakia"], "capital"])

print(staty.loc[["Slovakia", "Poland", "Austria", "Germany"], ["area", "population", "gini"]])