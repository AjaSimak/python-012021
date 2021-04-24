item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
key = "price"
item[key] = 929
#edituju si cenu
print("Vybraný předmět je " + item["title"] + " a cena je " + str(item["price"]) + ".")
print("Vybraný předmět je", item["title"], "a cena je", item["price"],".")
print(f"Vybraný předmět je {item['title']} a cena je {item['price']}.")
#musí tam být '', aby nebyl program zametný, že dvakrát ""
item["weight"] = 0.6
if "weight" in item:
    print(f"Hmotnost předmětu je {item['weight']}")
else:
    print("Hmotnost není zadána.")

sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
sausages.pop("Jirka")
#když pro Jirku nechci kelímek
print(len(sausages))
print(sausages)


