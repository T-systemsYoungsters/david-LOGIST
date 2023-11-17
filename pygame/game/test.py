# Import a library of functions called 'pygame'
import pygame
import math

pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.x=xpos
        self.y=ypos
        self.image=pygame.Surface((20,20))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.x= self.x
        self.rect.y= self.y
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Initialize the game engine

speed=3
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653
player = Player(200,200)
# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)
my_clock = pygame.time.Clock()

center_of_screen=(size[0]*0.5,size[1]*0.5)
 
# Loop until the user clicks the close button.
done = False
 
angle = 0
 
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

 
    # Set the screen background
    screen.fill(WHITE)
 
    # Dimensions of radar sweep
    # Start with the top left at 20,20
    # Width/height of 250
    box_dimensions = [50, 50, 300, 300]
    radius=150
 
    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)
 
    # Draw a black box around the circle
    pygame.draw.rect(screen, BLACK, box_dimensions, 2)
 
    # Calculate the x,y for the end point of our 'sweep' based on
    # the current angle
    x = center_of_screen[0] + math.sin(angle) * radius
    y = center_of_screen[1] + math.cos(angle) * radius

    if x == player.rect.x:
        print("x=x")
 
    # Draw the line from the center at 145, 145 to the calculated
    # end spot
    player.update()
    screen.blit(player.image, (player.rect.x, player.rect.y))
    # Increase the angle by 0.03 radians
    angle = angle + .03
 
    # If we have done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI
 
    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()