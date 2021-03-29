#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teploty = pandas.read_csv("temperature.csv")
teploty_13112017 = teploty[teploty["Day"] == 13]
teploty_nechybove = teploty[teploty["AvgTemperature"] != -99]


pocet_dat_regiony = teploty_13112017.groupby("Region").count()


max_teplota_regiony = teploty.groupby("Region").max()
min_teplota_regiony = teploty_nechybove.groupby("Region").min()

prumerna_teplota_regiony = teploty_nechybove.groupby("Region")["AvgTemperature"].mean()
print(teploty_13112017)
print(teploty_nechybove)

print(pocet_dat_regiony)
print(prumerna_teplota_regiony)

print(max_teplota_regiony)
print(min_teplota_regiony)