import pygame, math

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite/fish. """

    # Methods
    def __init__(self, width, height, screen_size, radius):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        #Start in the middle of the screen
        self.x=screen_size[0]/2
        self.y=screen_size[1]/2
        self.screen_size=screen_size
        self.radius=radius
        self.image = pygame.Surface([width, height])
        '''replace with picture later'''
        self.image.fill((0,0,0)) #.load("./assets/cartoon_fish_6.svg").convert()
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
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        '''limit movement to center'''#make border round
        if self.rect.x < (self.screen_size[0]/2-self.radius):
            self.rect.x=self.screen_size[0]/2-self.radius
        if self.rect.x > (self.screen_size[0]/2+self.radius):
            self.rect.x=self.screen_size[0]/2+self.radius
        if self.rect.y < (self.screen_size[1]/2-self.radius):
            self.rect.y=self.screen_size[1]/2-self.radius
        if self.rect.y > (self.screen_size[1]/2+self.radius):
            self.rect.y=self.screen_size[1]/2+self.radius