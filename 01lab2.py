#David Vilhena Klein
#21.09.2023
#Pygame Lab 1.2 auf http://programarcadegames.com
#Berechnen des Flächeninhaltes eines Trapezes
import math

def flaecheTrapez(a, c, h):
    flaeche = (a+c)*h/2
    return flaeche

def hoeheTrapez(flaeche, a, c):
    hoehe = (2*flaeche)/(a+c)
    return hoehe

def diagonaleTrapez(a, b, c, d):
    e = math.sqrt((a*d**2+a**2*c-a*c**2-c*b**2)/(a-c))
    f = math.sqrt((a*b**2+a**2*c-a*c**2-c*d**2)/(a-c))
    return e, f

done = False

while done == False:
    print("""Trapezrechner.
    Wählen Sie aus :
    (1) Berechnung der Fläche
    (2) Berechnung der Höhe
    (3) Berechnung des Umfangs
    (4) Berechnung der Diagonalen
    (5) Exit""")
    match input():
        case "1":
            a = float(input("Geben Sie die Länge der Grundseite an :"))
            c = float(input("Geben Sie die Länge der Seite gegenüber an :"))
            h = float(input("Geben Sie die Länge der Höhe an :"))
            print("Der Flächeninhalt des Trapezes beträgt", flaecheTrapez(a, c, h), "Flächeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "2":
            flaeche = float(input("Geben Sie die Fläche an :"))
            a = float(input("Geben Sie die Länge der Grundseite an :"))
            c = float(input("Geben Sie die Länge der Seite gegenüber an :"))
            print("Die Höhe der Grundseite beträgt", hoeheTrapez(flaeche, a, c), "Längeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "3":
            a = float(input("Geben Sie die Länge der Seite a an :"))
            b = float(input("Geben Sie die Länge der Seite b an :"))
            c = float(input("Geben Sie die Länge der Seite c an :"))
            d = float(input("Geben Sie die Länge der Seite d an :"))
            print("Der Umfang des Trapezes beträgt", a+b+c+d, "Längeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "4":
            a = float(input("Geben Sie die Länge der Seite a an :"))
            b = float(input("Geben Sie die Länge der Seite b an :"))
            c = float(input("Geben Sie die Länge der Seite c an :"))
            d = float(input("Geben Sie die Länge der Seite d an :"))
            if a=c:
                input("Achtung: a darf nicht gleich c sein! Drücke Enter um dennoch fortzufahren :")
            print("Die Länge der Diagonalen e beträgt", diagonaleTrapez(a, b, c, d)[0], "Längeneinheiten.")
            print("Die Länge der Diagonalen f beträgt", diagonaleTrapez(a, b, c, d)[1], "Längeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "5":
            done = True
        case __:
            print("Ungültige Eingabe.")
            input("Drücken Sie Enter um fortzufahren:")
print("goodbye")