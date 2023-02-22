import snakemd
#dodanie pustego pliku
# nowy_dokument = snakemd.new_doc("pliki/nowy_plik")
# nowy_dokument.output_page()

from secrets import token_urlsafe
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
