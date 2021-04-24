import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv('nakupy.csv')

pozdrav = "Ahoj Andreo"

print(pozdrav[-6:])
# vypíše mi to posledních 6 znaků
# vezme to i mezeru - mezera je totiž jako normální znak

print(pozdrav[-6:-3])
# můžu si očistit data firmy v mailistu, kdy si takhle odstraním @

pozdrav = " Ahoj Andreo "
print(pozdrav.strip())
# likviduje mezery vně
#nebo mezery uvnitř print(pozdrav.strip().replace("  ", " "))

# ísto iloc se dá použít head (vypíše prvních pět), tail (vypíše posledních 5)
print(nakupy.head())
print(nakupy.tail())
# n=5 je dané napevno (povinný parametr), když chci méně nebo více, tak n=2 do těch kulatých závorek, nebo tam můžu napsat jen číslo
#print(nakupy.head(3))
#print(nakupy.tail(n=2))

print(nakupy.iloc[:5, 0])
#filtruje prvních 5 řádků a nultý sloupec

#pokud bych chtěla přidat částku - vložím si sznam pomocí hranatých závorek
print(nakupy.iloc[:5, [0, 3]])

#pokud chci jen omezit sloupce, a chci všechny řádky, tak dám jen :
print(nakupy.iloc[:, [0, 3]])
#iloc pracuje vždy s číslem řádku
