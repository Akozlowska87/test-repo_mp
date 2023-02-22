import snakemd
from secrets import token_urlsafe
import subprocess

#dodanie pustego pliku
# nowy_dokument = snakemd.new_doc("pliki/nowy_plik")
# nowy_dokument.output_page()


plik = f"pliki/pliki_generowne/{token_urlsafe(8)}"

plik_dokument = snakemd.new_doc(plik)

tekst = """
Litwo ojczyzno moja
tu jesteś jak zdowie
itd....
"""

plik_dokument.add_header("Siemaneczko")
plik_dokument.add_horizontal_rule()
plik_dokument.add_paragraph(tekst)
plik_dokument.add_code("from snakemd import *", lang="python")
plik_dokument.output_page()

command = ["pandoc", "-o", f"{plik}.docx", f"{plik}.md"]
ret_code = subprocess.run(command, capture_output=True)
print(ret_code)