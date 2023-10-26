#David Vilhena Klein
#13.09.2023
#Sinusfunktion mithilfe von Reihenaddition f(x) = x - x^3/3! + x^5/5! - ...

def fakultaet(a): #Funktion, die Fakultaet berechnet (a!)
    for i in range(1,a):
        a = a * i
    return a


eingabe=float(input("Berechne Sinus von :")) #Eingabe
n=20 #Anzahl der Iterationen/Termen in der Summe
k=3 # Startwert für Exponenten und Fakultät
x=eingabe #Laufvariable für das Summieren der Terme in der Schleife

if eingabe > 4.5: #Warnung für falsche Ergebnisse, wenn ausser [-4,5|4,5] liegt
    input("Achtung: Das Ergebnis wird ungenau! Gib eine Zahl zwischen [-4,5|4,5] ein, für korrekte Ergebnisse. Drücke Enter um dennoch fortzufahren :")

for j in range(1,n+1): #Wiederhole n-mal
    if j%2==0: #Wenn j gerade ist, tue
        x = x + (eingabe**k)/fakultaet(k)
    elif j%2!=0: #Wenn j ungerade ist, tue
        x = x - ((eingabe**k)/fakultaet(k))
    k+=2 #K wird um zwei erhöht (3,5,7,9,...)
print("Der Sinus von", eingabe, "ist ", x) #Ausgabe des Ergebnisses