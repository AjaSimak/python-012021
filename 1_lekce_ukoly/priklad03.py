volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
hour = int(input("V kolik hodin chcete rezervovat místnost? "))
if hour in volnePokoje:
    room = volnePokoje.get(hour)
    print(f"Jsou dostupné tyto místnosti {room}.")
else:
    print ("Není volná žádná místnost.")