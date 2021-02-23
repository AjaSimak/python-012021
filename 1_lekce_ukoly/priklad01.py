baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
number = input("Zadej číslo balíku: ")
kuryr = baliky.get(number)
if kuryr==False:
    print("Balík nepředán kurýrovi.")
else:
    print("Balík předán kurýrovi.")