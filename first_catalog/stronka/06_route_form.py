from flask import Flask, render_template, request

DATABASE = "funkcje_dodatkowe/users.db"

from funkcje_dodatkowe.baza_danych import generate_token
from funkcje_dodatkowe.send_email_smarthost import mail_report
from datetime import datetime
from funkcje_dodatkowe.baza_danych import create_user_record
from funkcje_dodatkowe.baza_danych import check_mail

app = Flask("moja_apka)")
zmienna_m = 4

@app.route("/") #dekorator w python
def main_page():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def przechwyc_dane():
    pass

@app.route("/data")
def get_data():
    html = """
    <h2 Podaj nam dane </h2> <hr>
    Tu chcę Twój adres email: ...... <hr>
    """ + str(generate_token())
    return html

@app.route("/user/<value>")
def username(value):
    html = f"""
    <h1>Welcome new user</h1>
    Wysyłam Ci maila na adres: {value}
    """
    new_token = generate_token()
    mail_body = f"Treść naszego maila - {datetime.today()} - http://127.0.0.1:5000/clicked/{value}/{new_token}"

    if value.count("@") == 1:
        ret, ret_value = mail_report(value, "python-course@jurkiewicz.tech", mail_body)
        if ret == False:
            print(ret_value)
        if ret == True:
            retdb = create_user_record(DATABASE, value, new_token)
            print(f"Return - {retdb}")
    return html

@app.route("/clicked/<mail>/<value>")
def username_click(mail, value):
    html = f"""
    <h1>A jednak kliknięto</h1>
    Dla: {mail} - Wartość hash: {value} <hr>
    """
    sprawdzono = check_mail(DATABASE, mail, value)
    html += f"Czy się zgadza = {sprawdzono}"
    return html

app.run()