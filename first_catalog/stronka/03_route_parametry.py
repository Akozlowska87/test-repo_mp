from flask import Flask
from funkcje_dodatkowe.baza_danych import generate_token
from funkcje_dodatkowe.send_email_smarthost import mail_report
from datetime import datetime

app = Flask("moja_apka)")
zmienna_m = 4
@app.route("/") #dekorator w python
def main_page():
    return "<H1> Welcome</H1>"

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
    if value.count("@") == 1:
        ret, ret_value = mail_report(value, "python-course@jurkiewicz.tech", f"treść naszego maila - {datetime.today()}")
        if ret == False:
            print(ret_value)
    return html

app.run()