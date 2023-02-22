import csv
from faker import Faker
ludzik = Faker("pl-PL")

with open("pliki/ludzie.csv", "w" , newline="") as plik_csv:
    csv_writer = csv.writer(plik_csv, quoting=csv.QUOTE_NONNUMERIC) #delimiter=" ", quotechar="|",
    for _ in range(101):
        csv_writer.writerow([ludzik.name(), ludzik.company(), ludzik.company_vat(), ludzik.local_regon()])
