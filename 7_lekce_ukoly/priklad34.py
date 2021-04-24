#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
import matplotlib.pyplot as plt

velikonoce = pandas.read_csv("velikonoce.csv")
print(velikonoce.head())
#velikonoce.plot()
ax = velikonoce.plot("Datum")
ax.set_ylabel("Počet dnů")
ax.set_xlabel("Datum")
ax.set_title("Velikonoce")
ax.legend(loc=2)

plt.show()

#https://coobas.gitlab.io/python-fjfi/posts/matplotlib.html