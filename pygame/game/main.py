"""
David Vilhena Klein
08.11.2023

Growing fish game. Inspiration: Tasty Blue on Steam.
Final Lab on http://programarcadegames.com/

Graphics from https://www.gamedeveloperstudio.com

Implement next time: zweite runde, json, player radius,können sich untereinander fressen,
 no radius at map border, endless mode
"""
 
import pygame, random
from backround import *
from player import Player
from enemies import *
from menu import *
 

def main():
    """ Main function for the game. """
    pygame.init() #initiate pygame Module
    instructions() #Write instrucions into Console

    # Set the width and height of the screen [width,height]
    # Set the height and width of the screen
    # Define Map size
    # initiate Winodw
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    MAP_WIDTH = 2000
    MAP_HEIGHT = 2000
    screen = pygame.display.set_mode([SCREEN_WIDTH,  SCREEN_HEIGHT])
    pygame.display.set_caption("Fischsuppe")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Initiate Sprite.Group for all Sprites and only Enemy Sprites
    # convenient: the Sprite.Group.update() function
    all_sprites_list = pygame.sprite.Group()
    enemy_sprites_list = pygame.sprite.Group()

    #initiate the player
    # use of Class player.Player()
    #Initiate Game variables
    #Import Sound files
    player_radius=200
    player_size=50
    player=Player((SCREEN_WIDTH, SCREEN_HEIGHT), player_radius, player_size)
    speed_original=10 # Original speed to reset after dash
    speed=10 #Player movement speed
    score=0
    difficulty = 4 #Quantity of Enemies multiplied by factor
    numberofenemies=0 #Quantity of all Enemies for End of Game
    cooldown_hurt = 0 
    cooldown_killstreak = 0
    killstreak_text_cooldown=0
    # For Killstreak, random.choice out of following options:
    streaklist=["Munch Munch", "Pop", "sizzle", "crunch", "slurp", "munch", "gulp", "rustle"]
    sound=True # if True, the game starts with sound enabled, 
    sfx=True
    # be sure to change attributes in Window class as well!
    
    burp_sound = pygame.mixer.Sound("assets/burp.ogg")
    nom_sound = pygame.mixer.Sound("assets/nom.ogg")
    hurt_sound = pygame.mixer.Sound("assets/hurt.ogg")
    game_won_sound = pygame.mixer.Sound("assets/game.ogg")
    

    #initiate the backround from class backround.Backround()
    #initiate Menu window as a sprite from menu.Window()
    # x and y pos for screen offset
    backround = Backround("assets/pool.jpeg",SCREEN_WIDTH,SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT, player_radius)
    menu_window = Window()
    window_xpos=420
    window_ypos=200
    show_window = False #Only show Window when set to True
    

    """Show Game Intro and Loading animation""" #from menu.game_intro()
    game_intro(screen)
    
    #add backround to sprite-group, so it is drawn first
    #initiate 4 types of enemies and append to sprite-group
    # enemies' classes from enemy.py
    # Quantity of enemies depended on difficulty
    #(This takes some time, before the game can start)
    all_sprites_list.add(backround)

    for i in range(difficulty*4): #Starfish
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        star=Starfish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(star)
        all_sprites_list.add(star)

    for i in range(difficulty*4): #Normal Fish
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        fish=Fish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(fish)
        all_sprites_list.add(fish)
    
    for i in range(difficulty*2): #Crabs
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT//2,MAP_HEIGHT-200)
        crab=Crab(x,y,random.randrange(70,200))
        enemy_sprites_list.add(crab)
        all_sprites_list.add(crab)

    for i in range(difficulty): # Jellyfish
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        jelly=Jelly(x,y,random.randrange(50,200))
        enemy_sprites_list.add(jelly)
        all_sprites_list.add(jelly)

    # finally add player to sprite-group
    all_sprites_list.add(player)
    
    
    # Loop until the user clicks the close button.
    done = False
    """ -------- Main Program Loop ----------- """
    while not done:
        
        # START of EVENT PROCESSING ---------------------
        for event in pygame.event.get(): #Go through every event
            if event.type == pygame.QUIT: 
                done = True #exit Main Program Loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Show pause Window when ESC
                    show_window = True
                elif  event.key == pygame.K_SPACE:
                    # Dash when hitting SPACE
                    speed=50
            #change player.change according to moving direction, use WASD or Arrowkeys
            #The proper movement is calculated during player.update()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = -speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = -speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = speed
            elif event.type == pygame.KEYUP:
            #reset player.change if key is lifted
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = 0
        # End of EVENT PROCESSING ------------------------------
 
        # Start of GAME LOGIC ----------------------------------


        '''limit movement to center'''#make border round
        if player.rect.x < (player.x-player.radius):
            player.rect.x=player.x-player.radius
            backround.change_x=speed
        if player.rect.x > (player.x+player.radius-player_size):
            player.rect.x=player.x+player.radius-player_size
            backround.change_x=-speed
        if player.rect.y < (player.y-player.radius):
            player.rect.y=player.y-player.radius
            backround.change_y=speed
        if player.rect.y > (player.y+player.radius-player_size):
            player.rect.y=player.y+player.radius-player_size
            backround.change_y=-speed
        
        for i in enemy_sprites_list: #go through every enemy sprite
            # draw the enemies in dependence of the screen offset
            i.rect.x = i.xpos + backround.rect.x
            i.rect.y = i.ypos + backround.rect.y

            #if enemy is out of map, reset on other side of the screen
            # newposition is set randomly
            if i.xpos < 0: #too left
                i.xpos = MAP_WIDTH
                if i.iscrab == False: #ignore the crabs since they should only move left-right
                    i.ypos = random.randrange(1,MAP_HEIGHT) 
            elif i.xpos > MAP_WIDTH : #too right
                i.xpos = 0
                if i.iscrab == False:
                    i.ypos = random.randrange(1,MAP_HEIGHT)
            if i.ypos < 0 : #too up
                i.ypos = MAP_HEIGHT
                if i.iscrab == False:
                    i.xpos = random.randrange(1,MAP_WIDTH)
            elif i.ypos > MAP_HEIGHT : #too down
                i.ypos = 0
                if i.iscrab == False:
                    i.xpos = random.randrange(1,MAP_WIDTH-200)

            #---------------collision detection----------------
            player_hit = pygame.Rect.colliderect(player.hitbox, i.rect)
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
                    current_streak=random.choice(streaklist)
                    
            
        
            
        
        
        
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        draw_text(screen, "Score: "+str(score), 30, (0,0,0), 50, 50)

        # Draw fancy effect text on screen if killstreak
        # disable with sfx = False
        if killstreak_text_cooldown > 0:
            if sfx == True:
                draw_text(screen, current_streak, 60, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), player.x+random.randint(0,player.size[0]), player.y+random.randint(0,player.size[0]))
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
                #----------Event Handling inside Pause Window ------------
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] > window_xpos+100 and pygame.mouse.get_pos()[0] < window_xpos+300:
                    # RESUME
                        if pygame.mouse.get_pos()[1] > window_ypos+150 and pygame.mouse.get_pos()[1] < window_ypos+210:
                            show_window = False
                    if pygame.mouse.get_pos()[0] > window_xpos+30 and pygame.mouse.get_pos()[0] < window_xpos+90:
                    # Sound Control   
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
                    if pygame.mouse.get_pos()[0] > window_xpos+315 and pygame.mouse.get_pos()[0] < window_xpos+370:
                    # SFX Control
                        if pygame.mouse.get_pos()[1] > window_ypos+menu_window.height-90 and pygame.mouse.get_pos()[1] < window_ypos+menu_window.height-30:
                            if menu_window.sfx == True:
                                menu_window.sfx=False
                                sfx=False
                                print("Special Effects OFF")
                                menu_window.update(score)
                            elif menu_window.sfx == False:
                                menu_window.sfx=True
                                sfx=True
                                print("Special Effects ON")
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
    print("goodbye.")
 
if __name__ == "__main__":
    main()