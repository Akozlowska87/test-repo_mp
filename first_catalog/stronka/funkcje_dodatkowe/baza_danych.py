from secrets import token_hex
print(f"bla bla bla - {__name__}/ to jest przetwarzane przy imporcie")
zmienna_m = 5

def generate_token():
    new_token = token_hex(60)
    print(new_token)
    return new_token