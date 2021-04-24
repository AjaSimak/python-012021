class Package:
  def __init__(self, address, weight):
    self.address = address
    self.weight = weight
    self.delivered = False

  def deliver(self):
    self.delivered = True

  def get_info(self):
    return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'


class ValuablePackage(Package):
  def __init__(self, address, weight, value):
    super().__init__(self, address, weight)
    self.value = value


ValuablePackage = ValuablePackage("Pisek", 4.5, 2000)
ValuablePackage.get_info()
ValuablePackage.deliver()
ValuablePackage.get_info()


class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position} a na úvazek {self.workload}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

class PartTimeEmployee(Employee):
  def getInfo(self):
    return f"{super().getInfo()} s úvazkem {self.workload}."
  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload
brigadnik = PartTimeEmployee("Jirka Pesik", "brigadnik ve skladu", 0.5)
print(brigadnik.getInfo(PartTimeEmployee))



