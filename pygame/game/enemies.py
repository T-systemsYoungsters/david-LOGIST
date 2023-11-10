import pygame
import random


class Enemy(pygame.sprite.Sprite):
    """ The class is the the enemy fish """

    # Methods
    def __init__(self,x, y, size):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.xpos=x
        self.ypos=y
        self.size = (size, size)
        self.iscrab=False

        # -- Attributes
        # Set speed vector
        """Set the speed random and exclude 0"""
        self.change_x = random.randrange(-5,5)
        self.change_y = random.randrange(-5,5)
        if self.change_x == 0:
            self.change_x = random.randrange(1,5)
        if self.change_y == 0:
            self.change_y = random.randrange(1,5)
        #Start in the middle of the screen
        self.image = pygame.Surface(self.size)
        self.image = pygame.image.load("./assets/star.png") #default image is starfish
        self.image = pygame.transform.scale(self.image, self.size)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        

    def resetspeed(self):
        self.change_x=0
        self.change_y=0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.xpos += self.change_x
        self.ypos += self.change_y
    
class Jelly(Enemy):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.image = pygame.image.load("./assets/jelly.png")
        self.image = pygame.transform.scale(self.image, self.size)

class Crab(Enemy):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.image = pygame.image.load("./assets/crab.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.change_y = 0
        self.iscrab=True

class Fish(Enemy):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        if self.change_x < 0:
            self.image = pygame.image.load("./assets/fish.png")
        else:
            self.image = pygame.image.load("./assets/fish2.png")
        self.image = pygame.transform.scale(self.image, self.size)

class Starfish(Enemy):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.image = pygame.image.load("./assets/star.png")
        self.image = pygame.transform.scale(self.image, self.size)

    def update(self):
        """ Find a new position for the player"""
        self.xpos += self.change_x
        self.ypos += self.change_y
        self.change_x = random.randrange(-1,1)
        self.change_y = random.randrange(-1,1)
