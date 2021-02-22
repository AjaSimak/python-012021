baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
number = input("Zadej číslo balíku: ")
kuryr = baliky.get(number)
if number in baliky:
    if baliky in kuryr(True):
        print(f"Balík byl předán kurýrovi.")
    else:
        print(f"Balík zatím nebyl předán kurýrovi.")
else:
    print(f"Číslo balíku není na seznamu.")