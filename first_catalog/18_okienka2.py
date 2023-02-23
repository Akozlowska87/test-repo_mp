# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Jak wygląda Twój poranek?")],
    [sg.Text("Jeżeli musisz wstać godzinę wczęśniej kliknij OK. Natomiast jeżeli wstajesz 30 minut wcześniej wybierz EXIT")],
    [sg.Text("'i' - UWAGA - jeżeli jedno zbierasz się o innej porze kliknij Inna")],
    [sg.OK(), sg.Exit(),sg.Button("Inna"), sg.Button("Get waluta")]
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

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Zdarzenie to:{event}, zwracany słownik to: {values}")


# koniec programu
window.close()
print("End of application")