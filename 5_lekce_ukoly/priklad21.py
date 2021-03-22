#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
akcie = pandas.read_csv("twlo.csv")

#print(akcie.info())
print(akcie.shape)
print(akcie.iloc[301])
print(akcie.iloc[:5])
print(akcie.head())

