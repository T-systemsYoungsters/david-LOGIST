"""
David Vilhena Klein
19.10.2023

Lab 12 on
http://programarcadegames.com/
"""
 
import pygame
import random
 
# The use of the main function is described in Chapter 9.
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():
    def __init__(self):
        self.x=random.randint(0,700)
        self.y=random.randint(0,500)
        self.height=random.randint(20,70)
        self.width=random.randint(20,70)
        self.x_speed=random.randint(-3,3)
        self.y_speed=random.randint(-3,3)
        self.color=(random.randint(0,255), random.randint(0,255),random.randint(0,255))
    def move(self):
        self.x+=self.x_speed
        self.y+=self.y_speed
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))
def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #All the rectangles in a list
    mylist=[]
    for i in range(500):
        mylist.append(Rectangle())
    for i in range(500):
        mylist.append(Ellipse())

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
        for rectangle in mylist:
            
            rectangle.draw(screen)
            #rectangle.move()
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