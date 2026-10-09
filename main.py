from sprint1 import weerstation
from sprint2 import sprint2
from API import weer_api


while True:
    print()
    print("=== SMART APP ===")
    print("1. Weerstation")
    print("2. Smart Controller")
    print("3. Huidig weer")
    print("4. Stoppen")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        weerstation.weerstation()

    elif keuze == "2":
        sprint2.smart_app_controller()

    elif keuze == "3":
        try:
            temperatuur = weer_api.huidige_temperatuur()
            print(f"Huidige temperatuur in Utrecht: {temperatuur} C")
        except:
            print("Het weer kon niet worden opgehaald.")

    elif keuze == "4":
        print("Het programma wordt afgesloten")
        break

    else:
        print("Ongeldige keuze")