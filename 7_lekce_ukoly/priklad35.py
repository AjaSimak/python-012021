#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
import matplotlib.pyplot as plt

teploty = pandas.read_csv("temperature.csv")

mesta = teploty[teploty["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])] [["City", "AvgTemperature"]]
print(mesta)

#druhý způsob, kdy budu mít 3 grafy odděleně -> mesta.groupby("City").plot(kind='box', whis=[0, 100])
mesta.boxplot(by="City", whis=[0, 100])

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html

plt.show()