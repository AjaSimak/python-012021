from datetime import datetime
now = datetime.today()
datum = now.strftime("%d.%m.%Y")
print(datum)

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = 10
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)