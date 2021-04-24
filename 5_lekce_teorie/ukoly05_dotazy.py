#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")

import pandas
jmena = pandas.read_csv('jmena.csv')
jmena = jmena.set_index("jméno")

#úkol 1
print(jmena.loc["Jiří"])

#úkol 2
print(jmena.loc[["Martin", "Zuzana", "Josef"]])

#úkol 3
print(jmena.loc[: "Josef"])

#úkol 4
print(jmena.loc["Martin":"Tereza"], "věk")

#úkol 5
print(jmena.loc["Libor":], "věk")

#úkol 6
print(jmena.loc[:, "věk":"původ"])

#úkol 2.1
print(jmena[jmena["věk"] > 60])

#úkol 2.2
print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"]< 100_000)])
jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)]

#úkol 2.3
#(jmena[(jmena["jména"], ["četnost" == "slovanský"] | ["četnost" == "hebrejský"])])
vybranaJmena = jmena[[jmena["původ"].isin([["slovanský", "hebrejský"])]
print(vybranaJmena[["jméno", "četnost"]])
print(vybranaJmena.shape)

#úkol 2.4
print(jmena)
vybranaJmena = jmena[jmena["svátek"].isin(["1.2.", "2.2.", "3.2." ])]
vybranaJmena["jméno"]




