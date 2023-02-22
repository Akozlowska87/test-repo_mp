from faker import Faker
ludzik = Faker(["pl-PL", "jp-JP"])

for _ in range(10):
    print(ludzik.name(), ludzik.address(), ludzik.iban(), ludzik.credit_card_full())