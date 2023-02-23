# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
try:
    #sprawdzenie
    aa = "a" + q
except NameError:
    print("Brak zmiennej")
except KeyError:
    print("Błedny klucz")
except Exception as e:
    print(e)