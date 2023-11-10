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
        self.sound=False
        self.sound_image=pygame.image.load("assets/sound.png")
        self.sound_image=pygame.transform.scale(self.sound_image, (50,50))
        #Put window in the middle of the screen
        self.image = pygame.Surface((self.width, self.height))

    def update(self, score):
        self.image.fill((230,230,255))
        pygame.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (30,30,30),(5,5,self.width-10, self.height-10), 3)
        self.image.blit(self.sound_image, (35, self.height-85))
        pygame.draw.rect(self.image, (200,200,200),(30, self.height-90, 60,60), 5)
        if self.sound==False:
            pygame.draw.line(self.image, (200,0,0), (35, self.height-35), (85, self.height-85),7)
        if self.won == True:
            draw_text(self.image, "YOU WON!", 50, (80,80,150), 100,20)
            pygame.draw.line(self.image, (80,80,150), (100,80), (320,80),4)
            draw_text(self.image, "Score: "+str(score), 30, (80,80,150), 20,100)
        else:
            draw_text(self.image, "PAUSE", 50, (80,80,150), 130,20)
            pygame.draw.line(self.image, (80,80,150), (120,80), (280,80),4)