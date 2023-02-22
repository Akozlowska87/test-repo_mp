# import czasu
# import time
# # liczony czas od 01.01.1970
# print(time.time())
#
# import datetime
# print(datetime.time())
# print(datetime.date.today())
#
# data = datetime.date.today()
# data_iso = data.isoformat()
# print(data_iso)
# print(data.year)
# print(data.day)

#-> losowanie liczby
# from random import randint
# number = randint(4, 60)
# print(number)

# from turtle import *
# shape("turtle")
# shapesize(10)
# image = fd(40)
# print(image) #-> obra znika bo sie kończy program dodaliśmy pętle niekończącą się
# while True:
#     pass

# -> rysowanie wielokąta
def wielokat(n, dl):
    for _ in range(n):
        fd(dl)
        rt(360//n)

from turtle import *
shape("turtle")
# shapesize(3)
# wielokat(7, 150)
for _ in range(30, 300,10): #-> od 30 długośc boku do 200, co 10
    wielokat(5, _)

# poniżej zapobiegamy zamknięcia okna
while True:
    pass
