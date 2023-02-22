import snakemd
#dodanie pustego pliku
# nowy_dokument = snakemd.new_doc("pliki/nowy_plik")
# nowy_dokument.output_page()

from secrets import token_urlsafe
plik = f"pliki/{token_urlsafe(8)}"
plik_dokument = snakemd.new_doc(pliki)
nowy_dokument.output_page()
