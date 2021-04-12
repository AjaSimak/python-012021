#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import matplotlib.pyplot as plt
import pandas

platy = pandas.read_csv("platy_2021_02.csv", header=None)
print(platy.head())

platy = pandas.Series([platy])
print(type(platy))

platy.hist("plat")
#platy["plat"].hist()
plt.show()