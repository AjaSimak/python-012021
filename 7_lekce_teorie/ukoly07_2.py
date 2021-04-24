import matplotlib.pyplot as plt
import pandas
from datetime import datetime
#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt")

callcentrum = pandas.read_csv("callcentrum.txt", header=None)

print(callcentrum.head())
callcentrum = pandas.Series([callcentrum])
print(type(callcentrum))

callcentrum.hist()
callcentrum.plot(kind="box", whis=[5, 95])

print(datetime.timestamp(datetime(callcentrum)))

plt.show()
plt.show()