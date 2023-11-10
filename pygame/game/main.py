"""
David Vilhena Klein
08.11.2023

Growing fish game. Inspiration: Tasty Blue on Steam.
Final Lab on http://programarcadegames.com/

Graphics from https://www.gamedeveloperstudio.com

Implement next time: json, können sich untereinander fressen, stehende gegner out of border
"""
 
import pygame, random
from backround import *
from player import Player
from enemies import *
from menu import *
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (140, 221, 255)
 
 
def main():
    """ Main function for the game. """
    pygame.init()
    instructions()

    # Set the width and height of the screen [width,height]
    # Set the height and width of the screen
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    MAP_WIDTH = 2000
    MAP_HEIGHT = 2000
    screen = pygame.display.set_mode([SCREEN_WIDTH,  SCREEN_HEIGHT])
    pygame.display.set_caption("Fischsuppe")

    all_sprites_list = pygame.sprite.Group()
    enemy_sprites_list = pygame.sprite.Group()

    #initiate the player
    player_radius=150
    player_size=50
    player=Player((SCREEN_WIDTH, SCREEN_HEIGHT), player_radius, player_size)
    speed_original=10
    speed=10
    score=0
    burp_sound = pygame.mixer.Sound("assets/burp.ogg")
    nom_sound = pygame.mixer.Sound("assets/nom.ogg")
    hurt_sound = pygame.mixer.Sound("assets/hurt.ogg")
    game_won_sound = pygame.mixer.Sound("assets/game.ogg")
    difficulty = 4
    numberofenemies=0
    cooldown_hurt = 0
    cooldown_killstreak = 0
    killstreak_text_cooldown=0
    sound=False

    #initiate the backround
    backround = Backround("assets/pool.jpeg",SCREEN_WIDTH,SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT, player_radius)

    #initiate Menu window as a sprite
    menu_window = Window()
    window_xpos=420
    window_ypos=200
    show_window = False

    all_sprites_list.add(backround)

    game_intro(screen)
    
    #initiate enemies
    for i in range(difficulty*4):
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        star=Starfish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(star)
        all_sprites_list.add(star)

    for i in range(difficulty*4):
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        fish=Fish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(fish)
        all_sprites_list.add(fish)
    
    for i in range(difficulty*2):
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT//2,MAP_HEIGHT-200)
        crab=Crab(x,y,random.randrange(70,200))
        enemy_sprites_list.add(crab)
        all_sprites_list.add(crab)

    for i in range(difficulty):
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        jelly=Jelly(x,y,random.randrange(50,200))
        enemy_sprites_list.add(jelly)
        all_sprites_list.add(jelly)

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
                if event.key == pygame.K_ESCAPE:
                    # Show pause Window when ESC
                    show_window = True
                elif  event.key == pygame.K_SPACE:
                    # Dash when hitting SPACE
                    speed=50
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = -speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = -speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = speed
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
            # draw the enemies in dependence of the screen offset

            i.rect.x = i.xpos + backround.rect.x
            i.rect.y = i.ypos + backround.rect.y

            if i.xpos < 0:
                i.xpos = MAP_WIDTH
                if i.iscrab == False:
                    i.ypos = random.randrange(1,MAP_HEIGHT) 
                    #ignore the crabs since they should only move left-right
            elif i.xpos > MAP_WIDTH :
                i.xpos = 0
                if i.iscrab == False:
                    i.ypos = random.randrange(1,MAP_HEIGHT)
            if i.ypos < 0 :
                i.ypos = MAP_HEIGHT
                if i.iscrab == False:
                    i.xpos = random.randrange(1,MAP_WIDTH)
            elif i.ypos > MAP_HEIGHT :
                i.ypos = 0
                if i.iscrab == False:
                    i.xpos = random.randrange(1,MAP_WIDTH)

            """collision detection"""
            player_hit = pygame.Rect.colliderect(player.rect, i.rect)
            if player_hit and player.size < i.size and cooldown_hurt == 0:
                cooldown_hurt=60
                if sound == True:
                    hurt_sound.play()
                print("Ouch")
                score-=500
                print("Score :", score)
            elif player_hit and player.size > i.size:
                numberofenemies-=1
                print(numberofenemies)
                all_sprites_list.remove(i)
                enemy_sprites_list.remove(i)
                player_size+=5
                player.changesize(player_size)
                
                if numberofenemies == 0 or cooldown_killstreak > 0:
                    score+=100 + i.size[0]*6
                    if sound == True:
                        burp_sound.play()
                    killstreak_text_cooldown=60
                else:
                    score+=100 + i.size[0]*4
                    if sound == True:
                        nom_sound.play()
                    cooldown_killstreak = 60
                    
            
        
            
        
        
        
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        draw_text(screen, "Score: "+str(score), 30, (0,0,0), 50, 50)

        # Draw text on screen if killstreak
        if killstreak_text_cooldown > 0:
            draw_text(screen, "KILLSTREAK!", 60, (200,50,50), SCREEN_WIDTH/2-120, SCREEN_HEIGHT-100)
            killstreak_text_cooldown-=1

        if cooldown_hurt != 0:
            cooldown_hurt -=1
        if cooldown_killstreak != 0:
            cooldown_killstreak -=1
        if speed != speed_original:
            speed = speed_original
            
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Game Over
        if numberofenemies == 0:
            if sound == True:
                game_won_sound.play(score)
            show_window=True
            menu_window.won=True

        """Pause function------------------------------"""
        while show_window == True:
            menu_window.update(score)
            screen.blit(menu_window.image,(window_xpos, window_ypos))
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                    # Show pause Window when ESC
                        show_window = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] > window_xpos+30 and pygame.mouse.get_pos()[0] < window_xpos+90:
                        if pygame.mouse.get_pos()[1] > window_ypos+menu_window.height-90 and pygame.mouse.get_pos()[1] < window_ypos+menu_window.height-30:
                            if menu_window.sound == True:
                                menu_window.sound=False
                                sound=False
                                print("Sound OFF")
                                menu_window.update(score)
                            elif menu_window.sound == False:
                                menu_window.sound=True
                                sound=True
                                print("Sound ON")
                                menu_window.update(score)
            pygame.display.flip()
        """----------------------------------------------"""
 
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