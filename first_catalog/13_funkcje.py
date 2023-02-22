def info_znak(liczba):
    znak = chr(liczba)
    co_zwracam = f"Litera to {znak}"
    return co_zwracam

imie = "Alicja"
wiek = 36
lista_02 = [51, 73, 68, 93, 113]
lista = [18, 54, 5, wiek, 98, 69, imie, 13, lista_02]

for element in lista:
    print(f"Wartość {element} ma typ {type(element)}")
    if isinstance(element, int):
        print(info_znak(element))
    elif isinstance(element, list):
        print(f"Teraz lista wewnętrza - {element}")
        for innyelement in element:
            print(info_znak(innyelement))
    elif isinstance(element, str):
        print(f"Teraz string - {element}")
        for innyelement in element:
            print(f"{innyelement=}")
            print(f"Litera wewnętrzna ma kod {ord(innyelement)}")
    else:
        print("ERROR")


