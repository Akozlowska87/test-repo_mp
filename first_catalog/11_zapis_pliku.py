klasa = [
    ("Alicja Kozlowska", 1987),
    ("Wiesław Kowalski", 1986),
    ("Tomasz Kanarek", 1981),
    ("Janusz Mock", 1956),
    ("Urszula Urban", 1982)
]

for person in klasa:
    print(f"{person=}")

for person, year in klasa:
    print(f"{person=}, rok urodzenia ->> {year}")

# zapis do pliku

with open("plik.txt", "w") as plik:
    plik.write("test 123")