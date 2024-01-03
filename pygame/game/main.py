"""
David Vilhena Klein
08.11.2023

Growing fish game. Inspiration: Tasty Blue on Steam.
Final Lab on http://programarcadegames.com/

Graphics from https://www.gamedeveloperstudio.com

Implement next time: put Window in sprite.Group(), set DIFFICULTY, playsound(), datentypen
"""
 
import pygame, random
from backround import *
from player import Player
from enemies import *
from menu import *
 

def main(skip_intro=False):
    """ Main function for the game. """
    pygame.init() #initiate pygame Module
    instructions() #Write instrucions into Console

    # Set the width and height of the screen [width,height]
    # Set the height and width of the screen
    # Define Map size
    # initiate Winodw
    SCREEN_WIDTH:int = 1200
    SCREEN_HEIGHT:int = 800
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
    #set game Constants
    #Initiate Game variables
    #Import Sound files
    PLAYER_RADIUS=200
    player_size=50
    player=Player((SCREEN_WIDTH, SCREEN_HEIGHT), PLAYER_RADIUS, player_size)
    SPEED_ORIGINAL=10 # Original speed to reset after dash
    speed=8 #Player movement speed
    score=0
    DIFFICULTY = 4 #Quantity of Enemies multiplied by factor
    numberofenemies=0 #Quantity of all Enemies for End of Game
    cooldown_hurt = 0 
    cooldown_killstreak = 0
    killstreak_text_cooldown=0
    PLAYER_GROWTH_RATE=4 #player growth after kill in pixel
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
    backround = Backround("assets/pool.jpeg",SCREEN_WIDTH,SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT, PLAYER_RADIUS)
    menu_window = Window()
    window_xpos=420
    window_ypos=200
    show_window = False #Only show Window when set to True
    

    """Show Game Intro and Loading animation""" #from menu.game_intro()
    game_intro(screen, skip_intro)
    
    #add backround to sprite-group, so it is drawn first
    #initiate 4 types of enemies and append to sprite-group
    # enemies' classes from enemy.py
    # Quantity of enemies depended on DIFFICULTY
    #(This takes some time, before the game can start)
    all_sprites_list.add(backround)

    for i in range(DIFFICULTY*4): #Starfish
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        star=Starfish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(star)
        all_sprites_list.add(star)

    for i in range(DIFFICULTY*4): #Normal Fish
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT)
        fish=Fish(x,y,random.randrange(10,100))
        enemy_sprites_list.add(fish)
        all_sprites_list.add(fish)
    
    for i in range(DIFFICULTY*2): #Crabs
        numberofenemies+=1
        x= random.randrange(MAP_WIDTH)
        y= random.randrange(MAP_HEIGHT//2,MAP_HEIGHT-200)
        crab=Crab(x,y,random.randrange(70,200))
        enemy_sprites_list.add(crab)
        all_sprites_list.add(crab)

    for i in range(DIFFICULTY): # Jellyfish
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

        '''limit movement to screen'''
        if player.rect.x < 0:
            player.rect.x=0
        if player.rect.x > SCREEN_WIDTH-player_size:
            player.rect.x=SCREEN_WIDTH-player_size
        if player.rect.y < 0:
            player.rect.y=0
        if player.rect.y > SCREEN_HEIGHT-player_size:
            player.rect.y=SCREEN_HEIGHT-player_size
        '''limit movement to box in center and move bg'''
        #move like normal if map border is reached tho
        if player.rect.x < (player.x-player.radius) and backround.rect.x !=0:
            player.rect.x=player.x-player.radius
            backround.change_x=speed
        if player.rect.x > (player.x+player.radius-player_size):
            if backround.rect.x != -MAP_WIDTH + SCREEN_WIDTH:
                player.rect.x=player.x+player.radius-player_size
                backround.change_x=-speed
        if player.rect.y < (player.y-player.radius) and backround.rect.y !=0:
            player.rect.y=player.y-player.radius
            backround.change_y=speed
        if player.rect.y > (player.y+player.radius-player_size):
            if backround.rect.y != -MAP_HEIGHT + SCREEN_HEIGHT:
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
            # see if hitbox.rect and sprite.rect are overlapping
            # process hit for player smaller and bigger then sprite
            player_hit = pygame.Rect.colliderect(player.hitbox, i.rect)
            if player_hit and player.size < i.size and cooldown_hurt == 0:
                cooldown_hurt=60
                if sound == True:
                    hurt_sound.play()
                print("Ouch")
                score-=500
                print("Score :", score)
            elif player_hit and player.size[0] - i.size[0] > 10:
                numberofenemies-=1
                print("Enemys left : ", numberofenemies)
                all_sprites_list.remove(i)
                enemy_sprites_list.remove(i)
                player_size+=PLAYER_GROWTH_RATE
                player.changesize(player_size)

                # bonus score for Killstreak
                if numberofenemies == 0 or cooldown_killstreak > 0:
                    score+=100 + i.size[0]*6
                    if sound == True: #Sound Setting
                        burp_sound.play()
                    killstreak_text_cooldown=60 #cooldown 1 second
                # normal kill
                else:
                    score+=100 + i.size[0]*4
                    if sound == True:
                        nom_sound.play()
                    cooldown_killstreak = 30 #cooldown 1/2 second
                    current_streak=random.choice(streaklist)

        # the pause window has to be drawn AFTER the rest so it is on top

        # show Window when End of Game is reached
        if numberofenemies == 0:
            if sound == True:
                game_won_sound.play(score)
            show_window=True
            menu_window.won=True
        
        # END of GAME LOGIC ----------------------------------------------

        # Start of DRAW on SCREEN -------------------------------
        # move all sprites
        # Draw all sprites on screen in order of Sprite.Group(), Backround first
        # They're not shown until screen.flip()
        # Draw Score Text above enemies
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
        if speed != SPEED_ORIGINAL:
            speed = SPEED_ORIGINAL
            
        # END of DRAW on SCREEN ---------------------

        # START of GAME LOGIC #2 ---------------------------------------
        
        """START of PAUSE loop---------------------------------------"""
        # This way, the game stays frozen
        while show_window == True:
            menu_window.pause(window_xpos, window_ypos, score)
            screen.blit(menu_window.image,(window_xpos, window_ypos))
            #Show (changes of) pause window on screen 
            sound = menu_window.sound
            sfx = menu_window.sfx
            show_window = menu_window.ispaused
            if menu_window.restart==True:
                print("Restart")
                pygame.quit()
                restart()
                break
            pygame.display.flip()
        """END of PAUSE loop ---------------------------------------------"""
 
        # Show drawn objects on main screen
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit IDE friendly
    pygame.quit()
    print("goodbye.")

#Restart main loop with skipping of key promt
def restart():
    main(True)

# Run main loop if Program is run
if __name__ == "__main__":
    main()