import pygame


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
        #Start in the middle of the screen
        self.image = pygame.Surface(self.size)
        self.image = pygame.image.load("./assets/star.png")
        self.image = pygame.transform.scale(self.image, self.size)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def resetspeed(self):
        self.change_x=0
        self.change_y=0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.resetspeed()
        