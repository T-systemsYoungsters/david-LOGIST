#David Vilhena Klein
#11.10.2023
#CLI based adventure game
#Lab 7 from http://programarcadegames.com

# Liste mit allen Räumen
room_list=[]
#Die Einzelnen Räume werden der Liste als jeweils eigene Liste hinzugefügt. Jeder Raum enthält die Info, welche Räume angrenzen.
room_list.append(["WESTFLÜGEL: \nIn einem riesigen Raum sind zahlreiche Desksharing-Tische, von denen nur an einem in der hintersten Ecke ein alter ehemalige Postbeamte grimmig in sein Thinkpad murmelt. Du solltest ihn besser nicht stören. \nÖstlich kommst du zurück zum Eingang.", None, 1, None, None])
room_list.append(["EINGANG: \nDer Pförtner lächelt dich an. Neben dir ist ein Fahrstuhl. \nÖstlich und westlich sind Büros, südlich der Flur.", 7, 2, 4, 0])
room_list.append(["OSTFLÜGEL: \nVor dir steht ein riesiges Hamsterrad. \nNach Westen kommst du wieder zurück zum Eingang.", None, None, None, 1])
room_list.append(["BETRIEBSRATSBÜRO: \nDu stehst in einem sehr unaufgeräumten Raum voller Plakate. Hinter einer duftenden Dampfwolke, siehst du einen Mitarbeiter an einem Waffeleisen. Wahrscheinlich bereitet er den Waffelklatsch vor. \nNach Osten geht es zurück in den Flur.", None, 4, None, None])
room_list.append(["FLUR: \nDer lange geräumige Gang ist bespickt mit vielen magenta Bildern, die Corporate Identity ausgesucht hat. \nNach Norden geht es zurück zum Eingang, überall sind Büros.", 1, 5, 6, 3])
room_list.append(["TEEKÜCHE: \nDu triffst drei Mitarbeitende am Wasserspender. Sie diskutieren über zu lange Arbeitszeiten. Sie scheinen sehr aufgebracht, du solltest sie besser nicht stören. Daneben steht eine Kaffeemaschine. \nNach Westen geht es zurück in den Flur.", None, None, None, 4])
room_list.append(["KONFERENZSAAL: \nGerade findet eine Unterweisung zum Thema Passwortsicherheit statt. Daneben findet eine Unterweisung zum Thema \"Wie schreibe ich mich in Unterweisungen ein?\" statt. \nNach Norden geht es zurük in den Flur.", 4, None, None, None])
room_list.append(["CAFETERIA: \nAuf einer Tafel vor dir stehen drei Gerichte, die du noch nie in deinem Leben gehört hast. Du zweifelst daran, dass es überhaupt schmecken könnte. Neben dir steht eine Maschine, um dein Essensguthaben aufzuladen. \nNördlich geht es zum Balkon. Südlich ist der Fahrstuhl.", 8, None, 1, None])
room_list.append(["BALKON: \nDu siehst eine Menge Tische und die Skyline von Berlin. In dir kommen Gefühle hoch, du verstehst aber nicht was für welche. \nNach Süden gehts zurück. ", None, None, 7, None])
current_room=1

print("Wilkommen in der Winterfeldstraße.")
#------ Main-Loop -------
done=False
while not done:
    print()
    print(room_list[current_room][0]) #Raumdiskription
    print()
    eingabe = input("Wohin möchtest du gehen? :").upper()
    #Gleiche den Input ab und ändere current_room
    print("eingabe", eingabe)
    if ["N", "NORDEN", "NORD"].count(eingabe)==1:
        if room_list[current_room][1] != None:
            current_room=room_list[current_room][1]
        else:
            print("Weiter gehts nicht.") #wenn es keinen angrenzenden Raum in die Richtung gibt
    elif ["O", "OSTEN", "EAST", "E"].count(eingabe)==1:
        if room_list[current_room][2] != None:
            current_room=room_list[current_room][2]
        else:
            print("Weiter gehts nicht.")
    elif ["S", "SOUTH", "SÜDEN"].count(eingabe)==1:
        if room_list[current_room][3] != None:
            current_room=room_list[current_room][3]
        else:
            print("Weiter gehts nicht.")
    elif ["W", "WEST", "WESTEN"].count(eingabe)==1:
        if room_list[current_room][4] != None:
            current_room=room_list[current_room][4]
        else:
            print("Weiter gehts nicht.")
    elif eingabe== "Q": #Quitfunktion
        done=True
    else: #Fehlerhafter Input
        print("Du hast selbst irgendwie noch nicht verstanden in welche Richtung du gehen willst.")
    print()

