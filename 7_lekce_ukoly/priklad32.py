#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

#import matplotlib.pyplot as plt
#import pandas

#platy = pandas.read_csv("platy_2021_02.csv", header=None)
#print(platy.head())

#platy = pandas.Series([platy])
#print(type(platy))

#platy.hist("plat", bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
#platy["plat"].hist()
#plt.show()

import matplotlib.pyplot as plt
import pandas

platy = pandas.read_csv('platy_2021_02.csv')
platy.hist(column='plat')
plt.show()
