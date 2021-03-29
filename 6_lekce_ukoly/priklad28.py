#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas
staty = pandas.read_json("staty.json")
evropa = staty[staty["region"] == "Europe"]
evropa_subregiony = evropa.groupby("subregion").count()
evropa_subregiony_population = evropa.groupby("subregion")["population"].sum()

#print(staty.head(7))
#print(staty.loc[1])
#print(staty.columns)
print(evropa)
print(evropa_subregiony)
print(evropa_subregiony_population)

