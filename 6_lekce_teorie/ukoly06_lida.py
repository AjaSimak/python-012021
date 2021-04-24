# 1.
# Načtěte dva datové sety studentů do oddělených pandas DataFrame
# a pomocí funkce concat je spojte do jednoho setu.

studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
# 2.
# Pokud studentovi chybí ročník, znamená to, že již nestuduje.
# Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta.
# Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?

print(f"Kolik studentů již nestuduje: {sum(studenti['ročník'].isnull())}")
print(f"Kolik jsou dálkoví studenti: {sum(studenti['kruh'].isnull())}")

# 3.
# Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově.
# Nadále budeme pracovat pouze s prezenčními studenty.

studenti = studenti.dropna()

# studenti = studenti.dropna(subset=["ročník", "kruh"])

# print(studenti.shape)
# print(sum(studenti["ročník"].isnull()))
# print(sum(studenti["kruh"].isnull()))

# 4.
# Zjistěte, kolik prezenčních studentů je v každém z oborů.

# print(studenti.groupby("obor").count())

# print(studenti.groupby("obor").size())

# 5.
# Zjistěte průměrný prospěch studentů v každém oboru.

# print(studenti.groupby("obor")["prospěch"].mean())

# 6.
# Načtěte datový set s křestními jmény.
# Proveďte join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.

# print(pandas.merge(studenti, jmena, on=["jméno"]))

# print(pandas.merge(studenti, jmena[["jméno", "pohlaví"]], on=["jméno"]))

# 7.
# Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.

studenti = pandas.merge(studenti, jmena[["jméno", "pohlaví"]], on=["jméno"])

print(studenti.groupby("pohlaví").count())
print(studenti.groupby("pohlaví").size())
