"""
David Vilhena Klein
01.11.2023

Growing fish game. Inspiration: Tasty Blue on Steam.
Final Lab on http://programarcadegames.com/

Graphics from https://www.gamedeveloperstudio.com
"""
 
import pygame
from player import Player

 
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
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("My Game")

    all_sprites_list = pygame.sprite.Group()

    #initiate the player
    player=Player(50,50, (screen_width, screen_height), 150)
    speed=10

    
    
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.change_x = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.change_y = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.change_y = 0
        player.update()
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        all_sprites_list.draw(screen)
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