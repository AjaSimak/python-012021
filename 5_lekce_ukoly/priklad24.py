#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")


import pandas
teplota = pandas.read_csv("temperature.csv")

print(teplota.info())
#print(teplota.head())
#print(teplota.tail())

print(teplota[teplota["City"] == "Prague"])
# průměrná hodnota je vysoká, jedná se nejspíše o Fahrenheita (32F = 0 stupňů Celsia)

print(teplota[teplota["AvgTemperature"] > 80])

print(teplota[(teplota["Region"] == "Europe") & (teplota["AvgTemperature"]> 60)])

print(teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)])


#import pytemperature
#df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
# dotaz na import

