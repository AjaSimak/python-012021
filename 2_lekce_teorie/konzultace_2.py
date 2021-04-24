staty = [
  {'name': 'Afghanistan', 'capital': 'Kabul', 'region': 'Asia', 'subregion': 'Southern Asia', 'population': 27657145,
   'area': 652230.0, 'gini': 27.8},
  {'name': 'Åland Islands', 'capital': 'Mariehamn', 'region': 'Europe', 'subregion': 'Northern Europe',
   'population': 28875, 'area': 1580.0},
  {'name': 'Tonga', 'capital': "Nuku'alofa", 'region': 'Oceania', 'subregion': 'Polynesia', 'population': 103252,
 'area': 747.0},
  {'name': 'Vanuatu', 'capital': 'Port Vila', 'region': 'Oceania', 'subregion': 'Melanesia', 'population': 277500,
   'area': 12189.0},
  {'name': 'Venezuela (Bolivarian Republic of)', 'capital': 'Caracas', 'region': 'Americas',
                      'subregion': 'South America', 'population': 31028700, 'area': 916445.0, 'gini': 44.8},
  {'name': 'Viet Nam', 'capital': 'Hanoi', 'region': 'Asia', 'subregion': 'South-Eastern Asia',
   'population': 92700000, 'area': 331212.0, 'gini': 35.6},
  {'name': 'Wallis and Futuna', 'capital': 'Mata-Utu', 'region': 'Oceania', 'subregion': 'Polynesia',
   'population': 11750, 'area': 142.0},
  {'name': 'Western Sahara', 'capital': 'El Aaiún', 'region': 'Africa', 'subregion': 'Northern Africa',
   'population': 510713, 'area': 266000.0},
  {'name': 'Yemen', 'capital': "Sana'a", 'region': 'Asia', 'subregion': 'Western Asia', 'population': 27478000,
   'area': 527968.0, 'gini': 37.7},
  {'name': 'Zambia', 'capital': 'Lusaka', 'region': 'Africa', 'subregion': 'Eastern Africa', 'population': 15933883,
   'area': 752612.0, 'gini': 54.6},
  {'name': 'Zimbabwe', 'capital': 'Harare', 'region': 'Africa', 'subregion': 'South Africa', 'population': 14240168,
   'area': 390757.0}]


"""soucet = 0
for radek in staty:
    if radek["region"] == "Africa":
        soucet = soucet + radek["population"]
print(soucet)

for radek in staty:
  if radek ["name"] == "South Africa":
  print(radek)"""

#zaokrouhlování#
cele_cislo = round(3.5465656)
print(cele_cislo)

dve_desetinna = round(3.546, 2)
print(dve_desetinna)

text = "smskadaleipocetznaku"
pocet_sms = len(text) // 180 + 1
#pocet_sms = math.ceil(len(text)/ 180)#
print(pocet_sms)
#plus jedna protože platím za každou započatou sms#
#nebo mat.ceil - zaokrouhlení nahodu lepší než celočíselné dělení#

cisla = [1, 15, 168, 3, 45]
print(max(cisla))

max_populatin = 0
for stat in staty:
  if stat["population"] > max_populatin:
    max_populatin = stat["population"]
  print(max_populatin)
#jdete od nuly, a pak přepíše, když najde další větší, na konci procházení najde to největší#

#řazení#
seznam = [18, 7, 6, 1]
for i in  range(3):
  for j in range(3):
    if seznam[j] > seznam[j + 1]:
      mensi_cislo = seznam[j + 1]
      vetsi_cislo = seznam[i]
      seznam[j] = mensi_cislo
      seznam[j + 1] = vetsi_cislo
print(seznam)
#jednička se dopracovala jen o jeden krok dopředu, ne úplně dopředu -> seznam je třeba projít 16x, ne pouze 4x#
#algoritmus má n2 -> 4 vstupní hodnoty = 16 vstupních operací#
#řeším dvěma cykly - vnější a vnitřní#
#trvá to pak dále -> 4x déle...#

seznam = [10, 7, 6 , 1]
for i in range(3):
    for j in range(3):
        if seznam[j] > seznam[j + 1]:
            seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
            # mensi_cislo = seznam[j + 1]
            # vetsi_cislo = seznam[j]
            # seznam[j] = mensi_cislo
            # seznam[j + 1] = vetsi_cislo
print(seznam)

slovnik = {
  "A": True,
  "B": False
  }
dotaz_na_balik = "A"
if slovnik(dotaz_na_balik) == True:
  print("Balík byl předán kurýrovi")
# == True už je zbytečné, protože před temi rovná se už je to pravda, a pak se na to ptám znova#
# proto je lepší psát tam to False

velikost_vyhry = {
  True: 100,
  False: 0
}
vyhra = True
print(velikost_vyhry[vyhra])

#https://realpython.com/python-boolean/ pravdivostní hodnoty#

konference = input("Byl zákazník na konferenci? [ano/ne] ")
#konference = konference == "ano" je to samé jako to níže#
if konference == "ano":
  konference = True
else:
  konference = False
