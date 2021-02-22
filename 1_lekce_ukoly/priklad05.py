prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
book = input("Zadejte název knihy: ")
sales = prodeje2020.get(book)
salesLastYear = prodeje2019.get(book)
prodeje2019["Past"] = 0
if book in prodeje2020:
    print(f"Prodej v roce 2020 byl {sales}.")
else:
    print("Kniha se v roce 2020 neprodávala.")
if book in prodeje2019:
    print (f"Prodej v roce 2019 byl {salesLastYear}.")
else:
    print("Kniha se v roce 2019 neprodávala.")
print(f"Prodej za oba roky byl {sales} + {salesLastYear}.")
