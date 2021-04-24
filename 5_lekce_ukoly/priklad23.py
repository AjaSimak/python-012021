#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

import pandas
vakcinace = pandas.read_csv("country_vaccinations.csv")

#print(vakcinace.info())

# úkol datum
print(vakcinace[vakcinace["date"] == "2021-03-10"][["country","total_vaccinations"]])

# úkol nad 1 mil.
print(vakcinace[(vakcinace["date"] == "2021-03-10") & (vakcinace["total_vaccinations"] > 1_000_000)][["country", "total_vaccinations"]])

# úkol min a max
print(vakcinace[(vakcinace["date"] == "2021-03-10") & (vakcinace["total_vaccinations"] > 100_000) | (vakcinace["total_vaccinations"] < 100)][["country", "total_vaccinations"]])

# dobrovolné úkoly
print(vakcinace[(vakcinace["date"] == "2021-03-10") | (vakcinace["date"] == "2021-03-11") & (vakcinace["country"].isin([["United Kingdom", "Finland", "Italy"]]))])
#proč u UK, Finska a Itálie to nevypiuje pouze tyto země a pro Japonsko níže to funguje?

print(vakcinace[(vakcinace["date"] >= "2021-03-03") & (vakcinace["date"] <= "2021-03-09") & (vakcinace["country"] == "Japan")])


#jak na proměnné - zkouška
#datum_jedna = vakcinace["date"] == "2021-03-10"
#datum_dva = vakcinace["date"] == "2021-03-11"
#print(vakcinace[(datum_jedna | datum_dva) & vakcinace["country"] == "Japan"])