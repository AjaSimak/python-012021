import pandas
teplota = pandas.read_csv("temperature.csv")

#print(teplota.head())
print(teplota.info())

print(teplota[(teplota["Day"] == 13) & (teplota["Country"] == "US")])


teplota_US = teplota[(teplota["Day"] == 13) & (teplota["Country"] == "US")]
print(teplota_US[teplota_US["City"].isin(["Washington","Philadelphia"])])


#dobrovolný doplněk
print(teplota_US.mean() [["AvgTemperature"]])
print(teplota_US.median() [["AvgTemperature"]])
print(teplota_US.var() [["AvgTemperature"]])
