import pygame


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite/fish. """

    # Methods
    def __init__(self, screen_size, radius, pixel_size = 50):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        #Start in the middle of the screen
        self.x=screen_size[0]/2
        self.y=screen_size[1]/2
        self.screen_size=screen_size
        self.radius=radius
        self.size=(pixel_size,pixel_size)
        self.image = pygame.Surface(self.size)
        self.image_right= pygame.image.load("./assets/cartoon_fish_right.png")
        self.image_right= pygame.transform.scale(self.image_right, (self.size))

        self.image_left= pygame.image.load("./assets/cartoon_fish_left.png")
        self.image_left= pygame.transform.scale(self.image_left, self.size)
        self.image_left_up= pygame.image.load("./assets/cartoon_fish_left_up.png")
        self.image_left_up= pygame.transform.scale(self.image_left_up, self.size)
        self.image_left_down= pygame.image.load("./assets/cartoon_fish_left_down.png")
        self.image_left_down= pygame.transform.scale(self.image_left_down, self.size)
        self.image_right_up= pygame.image.load("./assets/cartoon_fish_right_up.png")
        self.image_right_up= pygame.transform.scale(self.image_right_up, self.size)
        self.image_right_down= pygame.image.load("./assets/cartoon_fish_right_down.png")
        self.image_right_down= pygame.transform.scale(self.image_right_down, self.size)
        self.image_up= pygame.image.load("./assets/cartoon_fish_up.png")
        self.image_up= pygame.transform.scale(self.image_up, self.size)
        self.image_down= pygame.image.load("./assets/cartoon_fish_down.png")
        self.image_down= pygame.transform.scale(self.image_down, self.size)

        self.image.blit(self.image_right,(0,0))
        self.image.set_colorkey((0,255,0))
        

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
    def changesize(self,size):
        self.size=(size,size)
        self.image=pygame.Surface(self.size)
        self.image_right= pygame.image.load("./assets/cartoon_fish_right.png")
        self.image_right= pygame.transform.scale(self.image_right, (self.size))
        self.image_left= pygame.image.load("./assets/cartoon_fish_left.png")
        self.image_left= pygame.transform.scale(self.image_left, self.size)
        self.image_left_up= pygame.image.load("./assets/cartoon_fish_left_up.png")
        self.image_left_up= pygame.transform.scale(self.image_left_up, self.size)
        self.image_left_down= pygame.image.load("./assets/cartoon_fish_left_down.png")
        self.image_left_down= pygame.transform.scale(self.image_left_down, self.size)
        self.image_right_up= pygame.image.load("./assets/cartoon_fish_right_up.png")
        self.image_right_up= pygame.transform.scale(self.image_right_up, self.size)
        self.image_right_down= pygame.image.load("./assets/cartoon_fish_right_down.png")
        self.image_right_down= pygame.transform.scale(self.image_right_down, self.size)
        self.image_up= pygame.image.load("./assets/cartoon_fish_up.png")
        self.image_up= pygame.transform.scale(self.image_up, self.size)
        self.image_down= pygame.image.load("./assets/cartoon_fish_down.png")
        self.image_down= pygame.transform.scale(self.image_down, self.size)
        self.image.set_colorkey((0,255,0))

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.change_x < 0 and self.change_y < 0:
            self.image.blit(self.image_left_up, (0,0))
        elif self.change_x > 0 and self.change_y < 0:
            self.image.blit(self.image_right_up, (0,0))
        elif self.change_x < 0 and self.change_y > 0:
            self.image.blit(self.image_left_down, (0,0))
        elif self.change_x > 0 and self.change_y > 0:
            self.image.blit(self.image_right_down, (0,0))
        elif self.change_x > 0:
            self.image.blit(self.image_right, (0,0))
        elif self.change_x < 0:
            self.image.blit(self.image_left, (0,0))
        elif self.change_y > 0:
            self.image.blit(self.image_down, (0,0))
        elif self.change_y < 0:
            self.image.blit(self.image_up, (0,0))
        