"""
David Vilhena Klein
08.11.2023

Growing fish game. Inspiration: Tasty Blue on Steam.
Final Lab on http://programarcadegames.com/

Graphics from https://www.gamedeveloperstudio.com

Implement next time: enemy-movement and sound, start and pause window, score, penalty, json
"""
 
import pygame, random
from backround import *
from player import Player
from enemies import Enemy
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (140, 221, 255)
 
 
def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    # Set the height and width of the screen
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    MAP_WIDTH = 2000
    MAP_HEIGHT = 2000
    screen = pygame.display.set_mode([SCREEN_WIDTH,  SCREEN_HEIGHT])
    pygame.display.set_caption("Gemischte Fischplatte")

    all_sprites_list = pygame.sprite.Group()
    enemy_sprites_list = pygame.sprite.Group()
    

    #initiate the player
    player_radius=150
    player_size=50
    player=Player((SCREEN_WIDTH, SCREEN_HEIGHT), player_radius, player_size)
    speed=10
    score=0
    nom_sound = pygame.mixer.Sound("assets/nom.ogg")

    #initiate the backround
    backround = Backround("assets/ocean.jpeg",SCREEN_WIDTH,SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT, player_radius)
    
    all_sprites_list.add(backround)
    
    #initiate enemy to try
    for i in range(1,random.randint(10,40)):
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        enemy=Enemy(x,y,random.randrange(1,100))
        enemy_sprites_list.add(enemy)
        all_sprites_list.add(enemy)

    all_sprites_list.add(player)
    

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Loop until the user clicks the close button.
    done = False
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = -speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = -speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = speed
                elif event.key == pygame.K_SPACE:
                    player_size+=10
                    player.changesize(player_size)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = 0
        
        
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        '''limit movement to center'''#make border round
        if player.rect.x < (player.x-player.radius):
            player.rect.x=player.x-player.radius
            backround.change_x=speed
        if player.rect.x > (player.x+player.radius):
            player.rect.x=player.x+player.radius
            backround.change_x=-speed
        if player.rect.y < (player.y-player.radius):
            player.rect.y=player.y-player.radius
            backround.change_y=speed
        if player.rect.y > (player.y+player.radius):
            player.rect.y=player.y+player.radius
            backround.change_y=-speed
        
        for i in enemy_sprites_list:
            i.rect.x = i.xpos + backround.rect.x
            i.rect.y = i.ypos + backround.rect.y
            player_hit = pygame.Rect.colliderect(player.rect, i.rect)
            if player_hit and player.size < i.size:
                print("Ouch")
                score-=500
                print("Score :", score)
            elif player_hit and player.size > i.size:
                all_sprites_list.remove(i)
                enemy_sprites_list.remove(i)
                player_size+=10
                player.changesize(player_size)
                score+=100 + i.size[0]*2
                print("Score :", score)
                nom_sound.play()
        
        
        
        
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        draw_text(screen, "Score: "+str(score), 30, (0,0,0), 50, 50)
            
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()