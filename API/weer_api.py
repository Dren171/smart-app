import requests


def huidige_temperatuur():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current=temperature_2m"

    antwoord = requests.get(url)
    data = antwoord.json()

    temperatuur = data["current"]["temperature_2m"]

    return temperatuur