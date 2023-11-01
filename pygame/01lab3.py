#David Vilhena Klein
#21.09.2023
#Pygame Lab 1.3 auf http://programarcadegames.com
#Random Berechnungen
import math

def flaecheKreis(r):
    flaeche = math.pi*r**2
    return flaeche

def flaecheEllipse(r1, r2):
    flaeche = math.pi*r1*r2
    return flaeche

def flaecheGleichDreieck(h):
    flaeche = h**2*math.sqrt(3)/3
    return flaeche

def volumenKegel(r, h):
    volumen = math.pi*r**2*h/3
    return volumen

def volumenKugel(r):
    volumen = math.pi*r**3*4/3
    return volumen

done = False

while done == False:
    print("""Ausrechnen von random Dingen.
    Wählen Sie aus :
    (1) Fläche eines Kreises
    (2) Fläche einer Ellipse
    (3) Fläche eines gleichseitigen Dreieckes
    (4) Volumen eines Kegels
    (5) Volumen einer Kugel
    (6) Exit""")
    match input():
        case "1":
            r = float(input("Geben Sie die Länge des Radius' an :"))
            print("Der Flächeninhalt des Kreises beträgt", flaecheKreis(r), "Flächeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "2":
            r1 = float(input("Geben Sie die Länge des ersten Radius' an :"))
            r2 = float(input("Geben Sie die Länge des zweiten Radius' an :"))
            print("Der Flächeninhalt der Ellipse beträgt", flaecheEllipse(r1, r2), "Flächeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "3":
            h = float(input("Geben Sie die Länge der Höhe h an :"))
            print("Der Flächeninhalt des Dreiecks beträgt", flaecheGleichDreieck(h), "Flächeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "4":
            r = float(input("Geben Sie die Länge des Radius' an :"))
            h = float(input("Geben Sie die Länge der Höhe h an :"))
            print("Das Volumen des Kegels beträgt", volumenKegel(r, h), "Volumeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "5":
            r = float(input("Geben Sie die Länge des Radius' an :"))
            print("Das Volumen der Kugel beträgt", volumenKugel(r), "Volumeneinheiten.")
            input("Drücken Sie Enter um fortzufahren:")
        case "6":
            done = True
        case __:
            print("Ungültige Eingabe.")
            input("Drücken Sie Enter um fortzufahren:")
print("goodbye")