class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

#užívá se terminologie rodič a potomek; z potomka můžu volat funkci rodiče
# funkce init lze překrýt - lze překrýt rodiče potomkem (třeba tím workload), ale nemusím opakovat name, position apod. pomocí super().
# funkce by se neměly jmenovat stejně, protože se mi pak vyvolání jde tam, kde je nejblíž v konkrétní třídě
#to, že jsem napsala do závorky Employee - tak pozná program, že je propojená třída
class PartTimeEmployee(Employee):
  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload

brigadnik = PartTimeEmployee("Andrea Šimáková", "brigádnice ve skladu", 0.5)
print(brigadnik.getInfo())


