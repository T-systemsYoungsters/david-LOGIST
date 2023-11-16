import pygame
from backround import * #for drawtext function

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

def game_intro(screen):

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                
        screen.fill((255,255,255))
        text_size=115
        draw_text(screen, "Fischsuppe", text_size, (50,50,150), screen.get_size()[0]/4+40, screen.get_size()[1]/3)
        draw_text(screen, "hit SPACE to play", 50, (50,50,150), screen.get_size()[0]/3+80, screen.get_size()[1]/2)
        pygame.display.flip()
    
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
        self.new_highscore=False
        self.sound=True
        self.sfx=True
        self.sound_image=pygame.image.load("assets/sound.png")
        self.sound_image=pygame.transform.scale(self.sound_image, (50,50))
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

            # Show current Highscore or New Highscore! message
            if check_highscore(score) == True:
                self.new_highscore = True
            if self.new_highscore == True:
                draw_text(self.image, "NEW HIGHSCORE!", 30, (80,80,150), 20,150)
            else:
                file = open("highscore.txt","r")
                highscore= file.read()
                draw_text(self.image, "Highscore: " + str(highscore), 30, (80,80,150), 20,130)
        else:
            draw_text(self.image, "PAUSE", 50, (80,80,150), 130,20)
            pygame.draw.line(self.image, (80,80,150), (120,80), (280,80),4)

            # Draw Resume Button
            draw_text(self.image, "RESUME", 50, (80,80,180), 110, 150)
            pygame.draw.rect(self.image, (200,200,200),(100, 150, 200,60), 5)


def check_highscore(score):
    #function that updates the highscore in highscore.txt
    # return True if new Highscore was set 
    new_highscore = False
    file = open("highscore.txt","r")
    old_highscore= int(file.read())

    if score > old_highscore:
        file=open("highscore.txt","w")
        newText=str(score)
        file.write(newText)
        file.close()
        new_highscore = True
        print("New Highscore!")

    return new_highscore