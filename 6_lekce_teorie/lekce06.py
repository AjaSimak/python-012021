#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")



import pandas

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
#dělám proto, že místnosti jsou jen v názvu souboru, ale chybí mi to pak v datech -> proto z toho dělám sloupec
maturita = pandas.concat([u202, u203, u302],ignore_index=True)

#concat spojuje tabulky

#print(u202.head())

#odčištění dat pomocí odstranění - nyní hledám hodnotu pravda, kdy hodnota chybí
# na odstranění slouží dropna (lze rovnou u načtení dat - takže u read_pandas) a fillna
# NaN je neznámá hodnota, neznamená automaticky 0 (třebaa u teploty)

##print(u202[u202["znamka"].isnull()])

#print(maturita.head())
# každý soubor si uchoval číslo řádku + tam chybí čísla, která pandas vyřadil, protože neměla hodnotu

#print(maturita.loc[1])
# to dělá pak neplechu, protože vypíše 3 řádky s jedničkou -> takže ignore_index=True

#maturita.to_csv("maturita.csv", index=False)

#modul uložení do excelu
#maturita.to_excel("maturita.xlsx", index=False)

#joinování = dám tabulky vedle sebe (propojuji tabulku maturita a studenti
# znát typy joinů - inner (úplný průnik), left (privilegovaná tabulka vlevo), right, full(auto) (tabulky zůstanou obě) join (jako v power query)
studenti = pandas.read_csv("studenti.csv")

vysledky_se_jmeny = pandas.merge(maturita, studenti, how="left")
#print(maturita.shape)
#print(vysledky_se_jmeny.shape)
#porovnávám 2 tabulky, jak se změnil jejich tvar - po propojení mi zmizely 2 řádky a přidal se jeden sloupec
#joinování left a right je podle toho, jak to mám seřazené v té závorce
print(maturita.head())
print(vysledky_se_jmeny.head())
print(maturita[maturita["mistnost"].isnull()])
# chci vědět, kde mám v maturitě prázdné řádky

#jak vybrat merge https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html


