#This file is for troubleshooting only

def highscore(score):
    #function that updates the highscore in highscore.txt
    # return True if new Highscore was set 
    new_highscore = False
    file = open("highscore.txt","r")
    highscore= int(file.read())

    if score > highscore:
        file=open("highscore.txt","w")
        newText=str(score)
        file.write(newText)
        file.close()
        new_highscore = True

    return new_highscore
    
if __name__=="__main__":
    print(highscore(int(input("Enter Score:"))))