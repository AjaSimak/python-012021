#import wget
#wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
#wget pomůže stahovat věci z webu

import pandas
nakupy = pandas.read_csv('nakupy.csv')
#print(nakupy)
#od 0 do 10 je primární klíč
#nakupy.info()
print(nakupy.shape)
#vrátí to 11 řádek a 4 sloupce
#shape je něco jako seznam, podle indexu můžu vybrat konkrétní hodnotu
print(nakupy.shape[0])
#nula je jako první číslo pro řádky
print(nakupy.shape[1])
print(nakupy.columns)

# indexy - jak vybrat konkrétní nákup
print(nakupy.iloc[3])
#vypíše to 4. řádek - čísluje od nuly, data se vypíší po řádcích a ne po sloupcích
# tabulka = dataFrame v terminologii pandas => úložiště, kam můžu načíst tabulku
# iloc - vybere jeden řádek a ta se uloží do "série" (Series), která je jednorozměrná

print(nakupy.iloc[0:5])
#chci se podívat na začátek dat, zobrazím si prvních 5 řádků
#kdybych dala 8: a pak nic, tak do bude od 7 do konce
# když chci poslední tři řádky, tak napíšu [-3:]