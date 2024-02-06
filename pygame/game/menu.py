import pygame
from backround import * #for drawtext function
from highscore import Highscores

def instructions():
    print('''
        Welcome to >> Gemischte Fischplatte << !

        WASD or Arrows to move
        SPACE to dash
        ENTER or MOUSECLICK to start

        Watch out for bigger fish!
          ''')
    
def youwon(score):
    print("""
        YOU WON!
          
        Your total Score is {}!

""".format(score))

def game_intro(screen, skip=False):
    '''Game Intro'''
    # ask for User input (SPACE) before start
    # skip prompt if game was restarted
    skip_intro=skip
    intro = True

    screen.fill((255,255,255))
    text_size=115
    draw_text(screen, "Fischsuppe", text_size, (50,50,150), screen.get_size()[0]/4+40, screen.get_size()[1]/3)
    draw_text(screen, "hit SPACE to play", 50, (50,50,150), screen.get_size()[0]/3+80, screen.get_size()[1]/2)
    pygame.display.flip()

    while intro and not skip_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
    
    draw_text(screen, "Loading...", 50, (50,50,150), screen.get_size()[0]/2, screen.get_size()[1]*3/4)
    pygame.display.flip()

class Window(pygame.sprite.Sprite):
    def __init__(self, window_width = 400, window_height = 400):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.width = window_width
        self.height = window_height
        self.won=False
        self.sound=True
        self.sfx=False
        self.ispaused=False
        self.restart=False
        self.sound_image=pygame.image.load("assets/sound.png")
        self.sound_image=pygame.transform.scale(self.sound_image, (50,50))
        # load highscores by initiating Highscores class
        self.highscores=Highscores("highscores.json")
        self.update_highscore=True
        #Displays Name when entered with prompt
        self.playername=""
        self.input_blink_timer=60
        #Put window in the middle of the screen
        self.image = pygame.Surface((self.width, self.height))
        pygame.rect = self.image.get_rect()

    def update(self, score):
        # overdraw window
        # draw border line
        self.image.fill((230,230,255))
        pygame.draw.rect(self.image, (30,30,30),(5,5,self.width-10, self.height-10), 3)

        # draw sound icon
        # draw square around sound icon
        # draw red line if sound == False
        self.image.blit(self.sound_image, (35, self.height-85))
        pygame.draw.rect(self.image, (200,200,200),(30, self.height-90, 60,60), 5)
        if self.sound==False:
            pygame.draw.line(self.image, (200,0,0), (35, self.height-35), (85, self.height-85),7)

        # draw sfx icon
        # draw square around sound icon
        # draw red line if sfx == False
        draw_text(self.image, "SFX", 30, (0,0,0), self.width-85, self.height-80)
        pygame.draw.rect(self.image, (200,200,200),(self.width-90, self.height-90, 60,60), 5)
        if self.sfx==False:
            pygame.draw.line(self.image, (200,0,0), (self.width-85, self.height-35), (self.width-35, self.height-85),7)
        
        

        if self.won == True:
            draw_text(self.image, "YOU WON!", 50, (80,80,150), 100,20)
            pygame.draw.line(self.image, (80,80,150), (100,80), (320,80),4)
            draw_text(self.image, "Score: "+str(score), 30, (80,80,150), 20,100)

            # Draw Restart Button
            draw_text(self.image, "RESTART", 50, (80,80,180), 110, 320)
            pygame.draw.rect(self.image, (200,200,200),(100, 320, 200,60), 5)

            if self.update_highscore == False and self.highscores.checkhighscore(score) == True:
                if self.playername!="SAFED!":
                    self.update_highscore= True
            
            if self.update_highscore == True:
                draw_text(self.image, "NEW HIGHSCORE! Hit Enter to safe.", 13, (0,0,0), 80, 130)
                draw_text(self.image, self.playername, 30, (0,0,0), 180, 90)
                if self.input_blink_timer < 60: #every second, show/dont show promt
                    draw_text(self.image, "_", 30, (0,0,0), 180+len(self.playername)*15, 90, font="monospace")
                if self.input_blink_timer == 0:
                    self.input_blink_timer = 120 #duration for blink
                self.input_blink_timer-=1 #change every frame


            # Draw Highscores
            draw_text(self.image, "Highscores:", 30, (80,80,150), 120,140)
            for i in range(0,4):
                line= "{:<7}:{:>6}".format(self.highscores.highscore_list[i][1], self.highscores.highscore_list[i][0])
                draw_text(self.image, line, 30, (80,80,150), 70,173+30*i, font="monospace")
            
        else:
            # Draw Pause Button
            draw_text(self.image, "PAUSE", 50, (80,80,150), 130,20)
            pygame.draw.line(self.image, (80,80,150), (120,80), (280,80),4)

            # Draw Resume Button
            draw_text(self.image, "RESUME", 50, (80,80,180), 110, 150)
            pygame.draw.rect(self.image, (200,200,200),(100, 150, 200,60), 5)

    def pause(self, window_xpos, window_ypos, score):
        self.ispaused= True
        self.update(score)
        # START of EVENT HANDLING inside PAUSE window ---------------
        pygame.init()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                # Show pause Window when ESC
                    self.ispaused = False
                elif event.key == pygame.K_RETURN and self.update_highscore==True:
                    #Check if highscore was updated before and Check if score is new highscore
                    if self.playername =="":
                        self.playername ="PLAYER"
                    self.highscores.new_score(score, self.playername) #append new score to Board ONCE
                    self.highscores.update() #Update json
                    self.playername ="SAFED!"
                    self.update_highscore=False
                elif event.key == pygame.K_BACKSPACE and self.update_highscore==True and len(self.playername)>0:
                    self.playername= self.playername[:-1]
                #allow user to set highscore name up to 7 characters
                elif self.update_highscore==True and len(self.playername) <=6 and event.key != pygame.K_LSHIFT:
                    self.playername=self.playername+chr(event.key).upper()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > window_xpos+100 and pygame.mouse.get_pos()[0] < window_xpos+300:
                # RESUME or RESTART
                    if pygame.mouse.get_pos()[1] > window_ypos+150 and pygame.mouse.get_pos()[1] < window_ypos+210:
                        if self.won == False:
                            self.ispaused = False #Resume
                    if pygame.mouse.get_pos()[1] > window_ypos+320 and pygame.mouse.get_pos()[1] < window_ypos+380:
                        if self.won == True:
                            self.restart=True
                elif pygame.mouse.get_pos()[0] > window_xpos+30 and pygame.mouse.get_pos()[0] < window_xpos+90:
                # Sound Control   
                    if pygame.mouse.get_pos()[1] > window_ypos+self.height-90 and pygame.mouse.get_pos()[1] < window_ypos+self.height-30:
                        if self.sound == True:
                            self.sound=False
                            print("Sound OFF")
                            self.update(score)
                        elif self.sound == False:
                            self.sound=True
                            print("Sound ON")
                            self.update(score)
                elif pygame.mouse.get_pos()[0] > window_xpos+315 and pygame.mouse.get_pos()[0] < window_xpos+370:
                # SFX Control
                    if pygame.mouse.get_pos()[1] > window_ypos+self.height-90 and pygame.mouse.get_pos()[1] < window_ypos+self.height-30:
                        if self.sfx == True:
                            self.sfx=False
                            print("Special Effects OFF")
                            self.update(score)
                        elif self.sfx == False:
                            self.sfx=True
                            print("Special Effects ON")
                            self.update(score)