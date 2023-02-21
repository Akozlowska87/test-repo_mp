#petla iteracyjna + iterables
imie = "Alicja"
wiek = 36
lista_02 = [1, 3, 6, 9, 13]
lista = [18, 54, 5, wiek, 8, 9, imie, 13, lista_02]

for element in lista:
    print(f"Wartość {element} ma typ {type(element)}")
    if isinstance(element, int):
        print(f"Litera to {chr(element)}")
    else:
        print("ERROR")
