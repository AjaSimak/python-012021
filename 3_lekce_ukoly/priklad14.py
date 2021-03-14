class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.salary = 20000
    self.children = 6

  def get_net_salary(self):
    #self.cista_mzda = cista_mzda
    sazba_dane = 0.15
    sleva_dite = 1500
    dan = self.salary * sazba_dane - self.children * sleva_dite
    cista_mzda = self.salary - dan
    return f"Čistá mzda je {cista_mzda}."

andrea = Employee("Andrea", "analytik")
print(andrea.get_net_salary())

