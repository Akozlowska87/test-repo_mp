colors = ["red", "green"]

ile = int(input("Ile chcesz dodać kolorów: "))
for new in range (ile):
    new_color = input("Jaki chcesz kolor? ")
    colors.append(new_color)

print(colors)
for color in colors:
    print(f"{color=}")



