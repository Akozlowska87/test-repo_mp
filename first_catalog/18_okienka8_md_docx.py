# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import requests
import snakemd
import subprocess
import os
from secrets import token_urlsafe
from pathlib import Path
from datetime import date, timedelta
import matplotlib.pyplot as plt

TEMP_DIR = "pliki_tymczasowe"
NBP_URL= "https://api.nbp.pl/"
TODAY = date.today()
TODAY_ISO = TODAY.isoformat()

def init_dir():
    if not Path(TEMP_DIR).exists():
        os.mkdir(TEMP_DIR)

def generuj_dokument(code, start_date, end_date=TODAY_ISO):
    token = token_urlsafe(8)
    plik = f"{TEMP_DIR}/{token}"
    wykres_png = f"{plik}.png"
    wykres_md = f'{token}.png'
    tytul_wykresu = f"Wykres waluty {code} z data od {start_date} do {end_date}"
    url_address = f"http://api.nbp.pl/api/exchangerates/rates/A/{code}/{start_date}/{end_date}/"
    kursy = []
    req_get = requests.get(url_address)
    dane = req_get.json()
    for dane_z_dnia in dane['rates']:
        kursy.append(dane_z_dnia['mid'])
    X = [x for x in range(len(kursy))]
    plt.plot(X, kursy)
    plt.grid()
    plt.title(tytul_wykresu)
    # plt.show()
    plt.savefig(wykres_png )

    plik_dokument = snakemd.new_doc(plik)
    plik_dokument.add_header(tytul_wykresu)
    plik_dokument.add_element(snakemd.Paragraph([snakemd.InlineText("Wykres", url=wykres_md, image=True)]))
    try:
        plik_dokument.output_page()
    except Exception as e:
        sg.Popup(e, title="ERROR")

    return token

def test_inna():
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    try:
        nbp_test = requests.get(NBP_URL)
        status_nbp = nbp_test.status_code
    except Exception as e:
        sg.Popup(f"Error-> {e} | status_code -> -999", title="ERROR")
        status_nbp = -999

    if status_nbp == 200:
        sg.Popup(f"Połączono z {NBP_URL} - status OK")
    elif status_nbp == -999:
        sg.Popup(f"Brak interentu - zweryfikuja połączenie {NBP_URL} - sprawdź kabelek")

    else:
        sg.Popup(f"Brak internetu - zweryfikuja połączenie {NBP_URL}- code: {status_nbp}")

def tworz_docx(token_plik):
    os.chdir(TEMP_DIR+"/")
    command = ["pandoc", "-o", f"{token_plik}.docx", f"{token_plik}.md"]
    try:
        subprocess.run(command, capture_output=True)
        return True
    except:
        sg.popup_error("Zainstaluj pandoc")
        return False

#start aplikacji
init_dir()

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Jak wygląda wykres wartości waluty w czasie?")],
    [sg.Text("Jeżeli chcesz zobaczyc wykres wpisz poniższe dane i kliknij OK, jeżeli chcesz zamknąć okno wybierz EXIT")],
    [sg.Text("UWAGA! - wykres może dotyczyć 30 dni wstecz.")],
    [sg.Text("Podaj kod waluty (np.: 'CHF'"), sg.Input("Wpisz wartość")],
    [sg.Text("Ile dni wstecz wykres, max 90?"), sg.Input("")],
    [sg.OK(), sg.Exit(), sg.Button("Inna"), sg.Button("Get waluta")]
]
window = sg.Window("Twój poranek", app_layout)

# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("Użytkownik zamknął okno przeglądarki lub kliknął 'Exit'")
        break

    if event == "OK":
        waluta = values[0].upper()
        # https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
        data_poczatkowa = TODAY - timedelta(int(values[1]))
        plik = generuj_dokument(waluta, data_poczatkowa.isoformat())
        if tworz_docx(f"{plik}"):
            sg.Popup(f"Plik {plik}.md przetowrzony na DOCX")
        else:
            sg.popup_error("Błąd")

    if event == "Inna":
        test_inna()

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Zdarzenie to:{event}, zwracany słownik to: {values}")

# koniec programu
window.close()
print("End of application")