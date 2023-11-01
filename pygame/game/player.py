import pygame

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # Methods
    def __init__(self, width, height):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.x=200
        self.y=200
        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))#.load("./assets/cartoon_fish_6.svg").convert()
        self.image.set_colorkey((255,255,255))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

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