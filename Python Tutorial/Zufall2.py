import random



N1= int(random.random()*100)

N2=int(random.random()*100)

if N1 < N2 and N1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if N1 < 30 or N2 < 30:
    print("Eine der beiden ist kleiner als 30")

if N1 < 50 and N2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")