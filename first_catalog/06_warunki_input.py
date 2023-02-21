current_year = 2023

my_birthday = input("Podaj rok urodzenia: ")
print(f"{id(my_birthday)=}")
my_birthday = int(my_birthday)
print(f"{id(my_birthday)=}")

my_age = current_year - my_birthday
print(f"My age is {my_age}")

if my_age >= 18:
    print("You are adult")
    print("You are inteligent")
elif my_age < 0:
    print("ERROR")
else:
    print("You aren't young")
