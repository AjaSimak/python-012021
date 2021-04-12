#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")

print(twilio.head)

ax = twilio.plot("Date", "Close")
ax.set_ylabel("Cena v dolarech")
ax.set_xlabel("Datum")
plt.show()

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot()
plt.show()

# z datumu se stala osa y a zároveň jedna z proměnných