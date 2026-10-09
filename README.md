# smart App

Dit is smart-app, het is een project.


## Gebruik van AI

Ik heb ChatGPT gebruikt als hulp tijdens het maken van Sprint 3.

Ik heb AI gebruikt voor uitleg over:
- functies en imports
- het samenvoegen van Sprint 1 en Sprint 2
- try/except voor fouten
- het gebruiken van de Open-Meteo API
- het oplossen van foutmeldingen in Python

Voorbeeld van een verandering:

Eerst werd de code van het weerstation direct uitgevoerd wanneer het bestand werd geïmporteerd. Daarna heb ik de code in een functie gezet:

def weerstation():
    ...

Hierdoor kan het weerstation vanuit main.py worden gestart met:

weerstation.weerstation()

Ook heb ik met hulp van AI try/except toegevoegd zodat het programma niet crasht wanneer een bestand niet bestaat of wanneer de gebruiker verkeerde invoer geeft.

De code is daarna zelf getest en aangepast wanneer er fouten ontstonden.