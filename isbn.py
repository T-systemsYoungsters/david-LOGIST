#David Vilhena Klein
#21.09.2023
#gewichtete Prüfziffer wie bei einer ISBN-Nummer berechnen
pruefziffer = 0
zahl = input("Bitte geben Sie ihre Nummer ein, zu der Sie eine Prüfsumme berechnen wollen :")
for i in zahl:
    if int(i)%2 == 0:
        pruefziffer += int(i)*3
    else:
        pruefziffer += int(i)
print("Die gewichtete Quersumme lautet ", pruefziffer)
pruefziffer=10-pruefziffer%10
print("Die Prüfziffer lautet ", pruefziffer)
print("Ihre ISBN lautet ", zahl+str(pruefziffer%10))
