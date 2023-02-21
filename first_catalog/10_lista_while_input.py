colors = []

#teraz user podaje własne kolory
while True:
    new_color = input("Jaki chcesz kolor? ")
    if new_color.lower()== "koniec":
        break
    colors.append(new_color)

print(colors)
for color in colors:
    print(f"{color=}")
