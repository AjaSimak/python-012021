#objektově orientované programování - mám formulář a ten mi vyplní spousta lidí ->1 formulář = třída, lidi, kteří vyplňuj = objekty#
class Employee:
#každý název třídy začíná velkým písmenem!! proto všechny fce píseme s malým
  def take_holiday(self, days):
    if self.take_holidays >= days:
      self.take_holidays = self.take_holidays - days
      return "Dovolená schválena."
    else:
      return f"Můžeš si vzít pouze {self.holidays} dnů"

  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}"

#co je v závorkách u funkcí, tak to je paramtr (u __init__), to s tím self. je atribut

  """def __str__(self):
    return self.name + ", " + self.postition + ", " + str(self.holidays)
print(frantisek)
#nejvíc používané init a str"""

  def __init__(self, name, position):
    self.name = name
    self.position = position
 # musím dělat, init (self, name...) -> name je parametr init
 #ale ta informace se nedostane do get_info
 #potřebuji přeměnit parametr funkce na atribut, který nemusí být parametrem
 #např. self.holiday = 25 (nemusí tam být holidays a ani není v závorce jako parametr
 #napr. self.probation = True (nepovinný paramtr by byl v závorce probation=False)
 #stributy poznám tak, že začínají self.
frantisek = Employee("František Novák", "konstruktér")
#frantisek.name = "František Novák"
#frantisek.position = "konstruktér"
print(frantisek.get_info())
#během volání už self nedávám#
#třída je zpravidla jedna, ale můžeme mít víc objektů (víc Františků)#

klara = Employee("Klára Nová", "konstruktérka")
#klara.name = "Klára Nová"
#klara.position = "konstruktérka"
print(klara.get_info())
#printy můžu dát i pod sebe, objekty jsou na sobě nezávislé#

frantisek.take_holiday(80)


