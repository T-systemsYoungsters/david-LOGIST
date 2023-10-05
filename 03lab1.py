#David Vilhena Klein
#22.09.2023
#lab 3.1 on http://programarcadegames.com/
# Quiztime!

punkte = 0
anzahlFragen =0

def richtig():
    global punkte #damit funktion auf die variable des Hauptprogrammes zugreifen kann
    global anzahlFragen
    punkte +=1
    anzahlFragen+=1
    print("Das hast du toll gemacht!")

def falsch(loesung):
    global punkte
    global anzahlFragen
    punkte +=0
    anzahlFragen+=1
    print("Das war leider falsch. Die richtige Antwort ist :", loesung)
    input("Drücke Enter, um zur nächsten Frage zu gelangen :")

print("Quiztime!")

match input("Was ist 3+4? :"):
    case "7":
        richtig()
    case __:
        falsch("7")

match input("Wie lautet Obamas Nachname? :"):
    case "Obama":
        richtig()
    case "obama":
        richtig()
    case __:
        falsch("Obama")

match input("Wie heißt Frau Kepetry mit Vornamen? :"):
    case "Frauke":
        richtig()
    case "frauke":
        richtig()
    case __:
        falsch("Frauke")

match input("Was ist die Hauptstadt von Deutschland? :"):
    case "berlin":
        richtig()
    case "Berlin":
        richtig()
    case __:
        falsch("Berlin")

match input("Was ergibt 2+2*2? \n (A) 8 \n (B) 6 \n (C) 4 \n"):
    case "6":
        richtig()
    case "b":
        richtig()
    case "B":
        richtig()
    case __:
        falsch("(B)")


print("Toll gemacht! Deine Punktzahl ist :", punkte)
print("Bei", anzahlFragen, "Fragen sind das", round(punkte/anzahlFragen*100), "Prozent")
