"""
David Vilhena Klein
20.10.23
Use sprites to collect blocks.
Lab 13 on
http://programarcadegames.com/
"""
import pygame
import random

def draw_text(text, size, col, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, col)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = ( 51, 204,  51)
BLUE  = (   0,  0, 255)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([20, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

good_sound = pygame.mixer.Sound("good_block.ogg")
bad_sound = pygame.mixer.Sound("bad_block.ogg")
bump_sound = pygame.mixer.Sound("bump.wav")
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    good_block = Block(GREEN, 20, 15)
    bad_block = Block(RED, 20,15)
 
    # Set a random location for the good_ block
    good_block.rect.x = random.randrange(screen_width)
    good_block.rect.y = random.randrange(screen_height)

    # Set a random location for the bad_ block
    bad_block.rect.x = random.randrange(screen_width)
    bad_block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(good_block)
    all_sprites_list.add(good_block)
    bad_block_list.add(bad_block)
    all_sprites_list.add(bad_block)
 
# Create a BLUE player block
player = Player(350, 200)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
speed=2
 
# -------- Main Program Loop -----------
while not done:
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
    # Clear the screen
    screen.fill(WHITE)

    if player.rect.x > 680:
        player.rect.x=680
        bump_sound.play()
    if player.rect.x < 0:
        player.rect.x=0
        bump_sound.play()
    if player.rect.y < 0:
        player.rect.y=0
        bump_sound.play()
    if player.rect.y > 385:
        player.rect.y=385
        bump_sound.play()
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        good_sound.play()
        
    for block in bad_blocks_hit_list:
        score -= 1
        bad_sound.play()
    
    # Draw all the spites
    all_sprites_list.draw(screen)

    #Draw Scoreboard
    draw_text("Score:"+str(score), 30, BLACK, 136, 356)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()