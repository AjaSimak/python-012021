from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej množství cílové měny: "))
pozadovana_mena = input("Zadej cizí měnu (EUR, USD, GBP, DKK): ")

cena_v_korunach_EUR = prevodnik.convert('EUR', 'CZK', pozadovano_v_cilove_mene)
cena_v_korunach_USD = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
cena_v_korunach_GBP = prevodnik.convert('GBP', 'CZK', pozadovano_v_cilove_mene)
cena_v_korunach_DKK = prevodnik.convert('DKK', 'CZK', pozadovano_v_cilove_mene)

if pozadovana_mena == "EUR":
  print(cena_v_korunach_EUR)
elif pozadovana_mena == "USD":
  print(cena_v_korunach_USD)
elif pozadovana_mena == "GBP":
  print(cena_v_korunach_GBP)
else:
  print(cena_v_korunach_DKK)

