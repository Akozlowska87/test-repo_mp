def przelicz_walute(kod, wartosc, kurs):
    """
    Funcja zwracająca wartość dla danej waluty jaką chcesz wymienić
    :param kod: kod waluty jako symbol 3-liter np. chf
    :param wartosc: ile chcesz wymienić waluty?
    :param kurs: aktualny kurs tej waluty wg. NBP
    :return: wyliczona wartośc dla danej waluty, kursu i wartość
    """
    wart_zwracana = round(wartosc * kurs, 2)
    napis = f"Dla waluty {kod} - po kursie {kurs}, ilość {wartosc} to {wart_zwracana}"
    return napis
print(przelicz_walute("chf", 113.4, 4.8634))

przelicz_walute()
