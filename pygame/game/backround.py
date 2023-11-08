import pygame
class Backround(pygame.sprite.Sprite):
    def __init__(self, img, screen_width, screen_height, width, height, player_radius, x_pos=0, y_pos=0):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        #Start in the middle of the screen
        self.image = pygame.Surface([width, height])
        self.x_border=width - screen_width
        self.y_border=height - screen_height
        self.bg = pygame.image.load(img)
        self.bg = pygame.transform.scale(self.bg, (width, height))
        self.image.blit(self.bg, (x_pos, y_pos))
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0


    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the backround"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x < -self.x_border:
            self.rect.x=-self.x_border
        if self.rect.x > 0:
            self.rect.x=0           
        if self.rect.y < -(self.y_border):
            self.rect.y=-self.y_border
        if self.rect.y > (0):
            self.rect.y=0