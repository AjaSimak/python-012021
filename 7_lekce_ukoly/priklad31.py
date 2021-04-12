#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teploty = pandas.read_csv("temperature.csv")

#print(teploty.head)


teploty_13112017 = teploty[teploty["Day"] == 13]
print(teploty_13112017)

teploty_nechybove = teploty[teploty["AvgTemperature"] != -99]
print(teploty_nechybove)

teploty_razeni = teploty.sort_values(by="AvgTemperature", ascending=False)
print(teploty_razeni)

teploty_max = teploty.sort_values(by="AvgTemperature", ascending=False)
print(teploty_max["City"].head())

teploty_min = teploty.sort_values(by="AvgTemperature")
print(teploty_min["City"].head())

# kontrola print(teploty_min[["City", "AvgTemperature"]].head())



