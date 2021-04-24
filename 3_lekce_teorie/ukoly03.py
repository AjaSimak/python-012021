class Book:
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages
    self.price = price

  def getInfo(self):
    return f"Název knihy zní {self.title}, počet stránek je {self.pages} a stojí {self.price} Kč."
#protože uvnitř třídy je funkce, musím mít (self)

  def discount(self, discountValues):
    self.price *= (1 - discountValues/100)

kniha = Book("Maryša", pages = 259, price = 150)
#můžu si to pojmenovat, ať vím, kde co je - můžu i prohodit pořadí
print(kniha.getInfo())
kniha.discount(10)
print(kniha.getInfo())


class Package:
  def __init__(self, adresa, vaha):
    self.address = adresa
    self.weightInKilos = vaha
    self.delivered = False


class Book:
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages
    self.price = price

    def getInfo(self):
      print(f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč.")

    def discount(self, discountValue):
      self.price *= (1 - discountValue / 100)


babicka = Book("Babička", price=399, pages=240)

babicka.getInfo()

babicka.discount(10)
babicka.getInfo()


class Package:
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

  def deliver(self):
    self.delivered = True

  def getInfo(self):
    print(f"Adresa: {self.address}")
    print(f"Hmotnost: {self.weightInKilos}kg")
    print(f"Stav: {'doručeno' if self.delivered else 'nedoručeno'}")


balik = Package("Nádražní 1, Brno", 0.5)
balik.getInfo()
balik.deliver()
balik.getInfo()

# baliky = [balik, Package("Nam. Svobody 1, Brno", 1.2)]
#
# for b in baliky:
#    b.getInfo()
#
# print()
#
# for b in baliky:
#    b.deliver()
#    b.getInfo()

