from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()

class CurrencyRates:
  def convert(self, cilova_mena, zdrojova_mena, pozadovano_v_cilove_mene):
    self.cilova_mena = cilova_mena
    self.zdrojova_mena = zdrojova_mena
    self.pozadovano_v_cilove_mene = pozadovano_v_cilove_mene
    return cena_v_korunach

pozadovano_v_cilova_mene = int(input("Kolik požadujete v cílové měně? "))
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach.convert())

