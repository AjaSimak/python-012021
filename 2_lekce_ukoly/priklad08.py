def phoneNumber(delka):
  #delka = int(delka)#
  if len(delka) == 13:
    if "+420" in delka:
      return True
    else:
      return f"číslo nemá českou předvolbu"
  elif len(delka) == 9:
    return True
  else:
    return False

delka = input("Zadej telefonní číslo: ")
print(phoneNumber(delka))

def sms(text):
  pocet_sms = len(text) // 180 + 1
  cena = 3
  return f"Celkem zaplatíš {pocet_sms * cena} Kč."
text = input("Zadej text zprávy: ")
print(sms(text))