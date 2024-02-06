import json 

class Highscores():
    def __init__(self, file):
        self.file=file
        with open(file, "r") as highscore_file:
            self.highscore_list = json.load(highscore_file)

    def get_highscores(self, amount):
        for i in range(0,amount):
            print(self.highscore_list[i])
    
    def checkhighscore(self, score):
        new_highscore = False
        if score > self.highscore_list[3][0]:
            new_highscore = True
        return new_highscore

    def new_score(self, score, name = "PLAYER"):
        # insert new score into the list and sort it
        # return True if new highscore was reached
        self.highscore_list.append([score, name]) #append new score to list
        #sort list. Highest score first
        def select_first_element(tuple):
            #Callback function for sorted(). Returns the first element of a tuple as int()
            return int(tuple[0])
        
        self.highscore_list = sorted(self.highscore_list, key=select_first_element, reverse= True)
        self.update()
        

    def update(self):
        # overwrite current highscores file with updated list
        with open(self.file,"w") as highscore_file:
            json.dump(self.highscore_list, highscore_file)
