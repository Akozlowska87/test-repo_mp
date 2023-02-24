from secrets import token_hex

def generate_token():
    new_token = token_hex(60)
    print(new_token)
    return new_token