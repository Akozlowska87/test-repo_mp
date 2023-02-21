#petla iteracyjna + literki
#od a do z
#wersja pierwsza

alphabet = "abcdefghijklmnopqrstuvwxyz"

# for letter in alphabet:
#     print(f"Letter is {letter}")
#
# for letter in alphabet:
#     print(f"Letter is {letter}", sep=" ")
#     print(letter, end=" / ")

# zbior = (1, 3, 5, 7, 9)
# a, b, c, e, d = zbior
# print(c)

# colors = ("red", "blue", "green")
# for color in colors:
#     print(color)

for letter in enumerate(alphabet):
    print(f"Letter is {letter}")

for position, letter in enumerate(alphabet):
    print(f"Letter is {letter}, {position=}")
    if position == 7:
        print("Siódemka!!!!")