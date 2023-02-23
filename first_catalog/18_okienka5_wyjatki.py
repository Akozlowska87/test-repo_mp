try:
    #sprawdzenie
    aa = "a" + q
except NameError:
    print("Brak zmiennej")
except KeyError:
    print("Błedny klucz")
except Exception as e:
    print(e)