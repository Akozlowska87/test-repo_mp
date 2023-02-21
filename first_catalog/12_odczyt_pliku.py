# odczyt z pliku
dane_ludzi = []

# with open("pliki/plik_in.txt", "r") as plik:
#     dane = plik.read()
#     print(f"{dane=} / {type(dane)}")


# with open("pliki/plik_in.txt", "r") as plik:
#     dane = plik.readline()
#     print(f"{dane=} / {type(dane)}")

with open("pliki/plik_in.txt", "r") as plik:
    dane = plik.readlines()
    print(f"{dane=} / {type(dane)}")

# for line in dane:
#     print(f"{line.strip()}")

for line in dane:
    # print(f"{line.strip().split(',')}")
    pozycja_z_pliku = line.strip().split(',')
    nazwisko = pozycja_z_pliku[0].strip()
    rok_urodzenia = int(pozycja_z_pliku[1].strip())
    print(f"Przetworzone: {nazwisko=} rok: {rok_urodzenia=}")