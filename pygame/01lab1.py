#David Vilhena Klein
#21.09.2023
#Pygame Lab 1.1 auf http://programarcadegames.com
#Umrechnung von Celsius in Fahrenheit und umgekehrt

def fahrenheit(c):
    f = c * 1.8 +32
    return f

def celsius(f):
    c = (f-32) * 5/9
    return c

done = False

while done == False:
    match input("Wählen Sie aus : \n (1) Umrechnung von Celsius zu Fahrenheit \n (2) Umrechnung von Fahrenheit zu Celsius\n (3) Quit \n :"):
        case "1":
            eingabe = float(input("Geben Sie die Temperatur in Grad Celsius an :"))
            print(eingabe, "°C sind", fahrenheit(eingabe), "°F.")
        case "2":
            eingabe = float(input("Geben Sie die Temperatur in Grad Fahrenheit an :"))
            print(eingabe, "°F sind", celsius(eingabe), "°C.")
        case "3":
            done = True
        case __:
            print("Ungültige Eingabe.")
            input("Drücken Sie Enter um fortzufahren:")

print("goodbye")