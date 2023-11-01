#David Vilhena Klein
#05.10.2023
#Pygame Lab 4 auf http://programarcadegames.com
#Kamelspiel mit E-Scooter statt Kamel
import random

runde=0
bonus=0
meterGefahren=5
meterZumZiel=200
meterPolizei=0
scooterHitze=0
scooterAkku=5
polizeiBonus=0
done = False

print("Wilkommen zu Berlin-Scooter!")
print("Du hast gerade Klein-Timmy von seinem E-Scooter heruntergestoßen und musst fliehen! ")
print("Dein Ziel ist es, die Grenze nach Spandau zu überqueren, um den Berliner Behörden zu entfliehen!")

while done == False:
    
    # Auswahl
    print("\n(1) Boost")
    print("(2) Fahre im moderaten Tempo.")
    print("(3) Volle Fahrt voraus ohne Rücksicht auf Verluste!")
    print("(4) Pause einlegen.")
    print("(5) Status")
    print("(Q) \"Ich muss raus!\"\n")
    match input().upper():
        case "1":
            print(random.choice(["Du machst dir einen coolen Song auf deinen Flexpods an.", "Dir fällt ein, dass du zu Hause deinen Herd angelassen hast.", "Du ballerst dir einen Kong-Strong-Energydrink rein.", "Du kramst aus deiner Hosentasche ein paar Fussel und einen komisch schmeckenden TikTak."]))
            print("Du kannst jetzt schneller als davor fahren, doch die Polizei hat aufgeholt!")
            bonus+=random.randint(3,7)
            meterPolizei+=random.randint(12,20)+polizeiBonus
        case "2":
            if scooterAkku >0:
                meterRunde=random.randint(8,18)+bonus
                meterGefahren+=meterRunde
                print("Du hast", meterRunde, "Meter zurückgelegen.")
            else: 
                print("Du hast kein Akku mehr. Du fährst den E-Scooter wie ein normaler Roller.")
                print("Das demotiviert dich so sehr, dass du jetzt überhaupt nicht mehr schnel fährst.")
                bonus=0
                meterRunde=random.randint(1,10)
                meterGefahren+=meterRunde
                print("Du hast", meterRunde, "Meter zurückgelegen.")
            meterPolizei+=random.randint(8,15)+polizeiBonus
            scooterHitze+=1
            polizeiBonus+=1
        case "3":
            if scooterAkku>2:
                print("Du startest richtig durch.")
                print(random.choice(["Dabei überfährst du eine Katze.", "Dabei rempelst du drei Rentner an."]))
                meterRunde=random.randint(20,35)+bonus
                meterGefahren+=meterRunde
                print("Du hast", meterRunde, "Kilometer zurückgelegen.")
                scooterAkku-=2
                scooterHitze+=random.randint(1,3)
                meterPolizei+=random.randint(8,15)+polizeiBonus
                polizeiBonus+=1
            else:
                print("Du hast nicht genug Akku, um schnell zu fahren.")
        case "4":
            print(random.choice(["Du gönnst deinem Scooter das Kabel deiner Powerbank. Das entheddern dauert aber so lange, dass die Polizei aufholt.", "Du stoppst an einer E-Ladesäule."]))
            scooterAkku=random.randint(2,4)
            print("Du konntest den Scooter auf", scooterAkku, "laden und er ist nicht mehr heiß.")
            meterPolizei+=random.randint(5,12)+polizeiBonus
            scooterHitze=0

        case "5":
            print("Du hast bereits {} Kilometer zurückgelegt.".format(meterGefahren))
            random.choice(["Aber wieso fragst du überhaupt?", "Der Scooter machts inzwischen komische Geräusche.", "Du machst dir Sorgen wegen der Polizei."])
            print("Die Polizei ist", meterGefahren-meterPolizei, "km hinter dir!")
            print("Der Scooter ist {}/10 geladen.".format(scooterAkku))
        case "Q":
            done = True
        case __:
            print("Ungültige Eingabe.")
            input("Drücken Sie Enter um fortzufahren:")

    # --- Events, die zufällig eingestreut werden ---
    if random.randint(1,100)>95:
        print("Heute scheint nicht dein Tag zu sein. Die Mutter vom kleinen Timmy heißt Karen. Die Polizei ist jetzt schneller als sonst.")
        polizeiBonus+=3
        scooterAkku+=random.randint(1,3)
    if random.randint(1,100)<50:
        print("Du hast beim Vorbeifahren ein Handy abgezogen. Damit konntest du dein Scooter ein bisschen laden.")
        scooterAkku+=1
    
    # --- Bedingungen: Gewinnen, Verlieren oder Warnen
    if meterGefahren>=meterZumZiel:
        done=True
        print("Du hast nach", runde, "Runden erfolgreich die Grenze nach Spandau überquert. Die Berliner Polizei kann im Ausland nichts mehr ausrichten. Du hast gewonnen!")
    elif meterPolizei >= meterGefahren:
        done=True
        print("Du wurdest nach ", runde, "Runden festgenommen. Du hast verloren.")
    elif meterGefahren-meterPolizei < 10 : #Polizei holt auf
        print("Du hörst die Sirenen der Polizei, wie sie aufholen. Du solltest dich beeilen!")
    elif scooterHitze > 8: #
        print("Dein Scooter ist explodiert. Du bist tot. Hättest du den Scooter mal nicht überhitzen lassen...")
        done=True
    elif scooterHitze > 4:
        print("Dein Scooter fühlt sich ganz schön heiß an.")
    runde+=1
    
    