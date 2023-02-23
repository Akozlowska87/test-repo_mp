# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg


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

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Zdarzenie to:{event}, zwracany słownik to: {values}")


# koniec programu
window.close()
print("End of application")