import requests

url_address = "http://api.nbp.pl/api/exchangerates/tables/A/"
req_get = requests.get(url_address)
# print(req_get)
# print(req_get.text)
dane = req_get.json()
# print(type(dane))

# for element in dane:
#     print(element, type(element))
slownik_walut = dane[0]
# print(type(slownik_walut))
# print(slownik_walut.keys())
kursy_walut = slownik_walut["rates"]
# print(type(kursy_walut))
print(kursy_walut)

for waluta in kursy_walut:
    print (waluta, type(waluta))
    print(f"Dla {waluta['currency']} - kurs {waluta['mid']}")
