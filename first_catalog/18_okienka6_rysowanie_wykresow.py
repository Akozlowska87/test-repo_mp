import requests
import matplotlib.pyplot as plt # https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html

table = "A"
code = "EUR"
startDate = "2022-11-01"
endDate = "2023-02-21"
url_address = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{startDate}/{endDate}/"

kursy = []
req_get = requests.get(url_address)
dane = req_get.json()
# print(dane['rates'])
for dane_z_dnia in dane['rates']:
    kurs_z_dnia = dane_z_dnia['mid']
    kursy.append(kurs_z_dnia)

print(kursy)

X = [ x for x in range(len(kursy))]
plt.plot(X,kursy)
# plt.bar(X,kursy)
# plt.barh(kursy, X)
plt.grid()
plt.title(f"Wykres waluty {code} z data od {startDate} do {endDate}")
plt.show()