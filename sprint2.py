def aantal_dagen(inputFile):
    # Lees alle regels uit het bestand
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    # De eerste regel (namen van de kolommen) telt niet mee
    aantal = 0
    for i in range(1, len(regels)):
        if regels[i].strip() != "":
            aantal = aantal + 1

    return aantal


def auto_bereken(inputFile, outputFile):
    # Lees alle regels uit het inputbestand
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    # Open het outputbestand om in te schrijven
    uitvoer = open(outputFile, "w")

    # Begin bij 1, want regel 0 zijn de kolomnamen
    for i in range(1, len(regels)):
        regel = regels[i].strip()

        if regel != "":
            delen = regel.split()
            datum = delen[0]
            mensen = int(delen[1])
            setpoint = float(delen[2])
            buiten = float(delen[3])
            neerslag = float(delen[4])

            # CV ketel
            verschil = setpoint - buiten
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            # Ventilatie (maximaal 4)
            ventilatie = mensen + 1
            if ventilatie > 4:
                ventilatie = 4

            # Bewatering
            if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

            uitvoer.write(f"{datum};{cv};{ventilatie};{bewatering}\n")

    uitvoer.close()


def overwrite_settings(outputFile):
    # Vraag de gegevens aan de gebruiker
    datum = input("Datum (dd-mm-jjjj): ")
    systeem = input("Systeem (1=CV, 2=ventilatie, 3=bewatering): ")
    waarde = input("Nieuwe waarde: ")

    # Lees het outputbestand
    bestand = open(outputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    # Zoek de regel met de datum
    plek = -1
    for i in range(len(regels)):
        delen = regels[i].strip().split(";")
        if delen[0] == datum:
            plek = i

    if plek == -1:
        return -1

    # Zijn systeem en waarde hele getallen?
    try:
        systeem = int(systeem)
        waarde = int(waarde)
    except ValueError:
        return -3

    # Controleer of de waarde mag bij dit systeem
    if systeem == 1:
        if waarde < 0 or waarde > 100:
            return -3
    elif systeem == 2:
        if waarde < 0 or waarde > 4:
            return -3
    elif systeem == 3:
        if waarde != 0 and waarde != 1:
            return -3
    else:
        return -3

    # Pas de regel aan
    delen = regels[plek].strip().split(";")
    if systeem == 3:
        if waarde == 1:
            delen[3] = "True"
        else:
            delen[3] = "False"
    else:
        delen[systeem] = str(waarde)

    regels[plek] = f"{delen[0]};{delen[1]};{delen[2]};{delen[3]}\n"

    # Schrijf alles terug naar het bestand
    uitvoer = open(outputFile, "w")
    for regel in regels:
        uitvoer.write(regel)
    uitvoer.close()

    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    keuze = ""
    while keuze != "4":
        print()
        print("1. Aantal dagen")
        print("2. Auto berekenen")
        print("3. Waarde aanpassen")
        print("4. Stoppen")
        keuze = input("Keuze: ")

        if keuze == "1":
            aantal = aantal_dagen(inputFile)
            print(f"Aantal dagen: {aantal}")

        elif keuze == "2":
            auto_bereken(inputFile, outputFile)
            print("Output is geschreven.")

        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)
            if resultaat == 0:
                print("Aangepast!")
            elif resultaat == -1:
                print("Datum niet gevonden.")
            else:
                print("Ongeldig systeem of waarde.")

        elif keuze == "4":
            print("Tot ziens!")

        else:
            print("Ongeldige keuze.")


# Start het programma
if __name__ == "__main__":
    smart_app_controller()