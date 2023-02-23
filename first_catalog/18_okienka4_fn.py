# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import requests
import snakemd
import subprocess
import os
from secrets import token_urlsafe
from pathlib import Path

TEMP_DIR = "pliki_tymczasowe"
NBP_URL= "https://api.nbp.pl/"

def init_dir():
    if not Path(TEMP_DIR).exists():
        os.mkdir(TEMP_DIR)

def generuj_dokument():
    plik = f"{TEMP_DIR}/{token_urlsafe(8)}"
    plik_dokument = snakemd.new_doc(plik)
    try:
        plik_dokument.output_page()
    except Exception as e:
        sg.Popup(e, title="ERROR")

def test_inna():
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

#start aplikacji
init_dir()

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Jak wygląda wykres wartości waluty w czasie?")],
    [sg.Text("Jeżeli chcesz zobaczyc wykres wpisz poniższe dane i kliknij OK, jeżeli chcesz zamknąć okno wybierz EXIT")],
    [sg.Text("UWAGA! - wykres może dotyczyć 30 dni wstecz.")],
    [sg.Text("Podaj kod waluty (np.: 'CHF'"), sg.Input("Wpisz wartość")],
    [sg.Text("Ile dni wstecz wykres, max 30?"), sg.Input("")],
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
        generuj_dokument()

    if event == "Inna":
        test_inna()

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Zdarzenie to:{event}, zwracany słownik to: {values}")

# koniec programu
window.close()
print("End of application")