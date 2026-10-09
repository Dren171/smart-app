def weerstation():
    temperaturen = []

    for dag in range(1, 8):

        temp = input(f"Wat is op dag {dag} de temperatuur[C]: ")

        if temp == "":
            break

        try:
            temp = float(temp.replace(",", "."))
        except ValueError:
            print("Voer een geldig getal in.")
            break

        wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")

        if wind == "":
            break

        try:
            wind = float(wind.replace(",", "."))
        except ValueError:
            print("Voer een geldig getal in.")
            break

        vochtigheid = input(f"Wat is op dag {dag} de vochtigheid[%]: ")

        if vochtigheid == "":
            break

        try:
            vochtigheid = float(vochtigheid.replace(",", "."))
        except ValueError:
            print("Voer een geldig getal in.")
            break

        # berekeningen
        # Fahrenheit berekenen
        fahrenheit = 32 + 1.8 * temp

        # Gevoelstemperatuur berekenen
        gevoel = temp - vochtigheid / 100 * wind

        # Temperatuur opslaan
        temperaturen.append(temp)

        print(f"Het is {temp:.1f}C ({fahrenheit:.1f}F)")

        # Weerrapport
        if gevoel < 0:
            if wind > 10:
                print("Het is heel koud en het stormt")
            else:
                print("Het is behoorlijk koud")

        elif gevoel < 10:
            if wind > 12:
                print("Het is best koud en het waait")
            else:
                print("Het is een beetje koud")

        elif gevoel < 22:
            print("Heerlijk weer")

        else:
            print("Heel warm")

        print(f"Gem. temp tot nu toe is {sum(temperaturen) / len(temperaturen):.1f}")
        print("=" * 38)

    print("B bye")