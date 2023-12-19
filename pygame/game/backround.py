import pygame

def draw_text(screen,text, size, col, x, y, font = "arial"):
        """Draw Text on the screen"""
        font_name = pygame.font.match_font(font)
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, col)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)    
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

    def resetspeed(self):
        self.change_x=0
        self.change_y=0

    def check_corner(self):
        corner = False
        if self.rect.x < -self.x_border:
            self.rect.x=-self.x_border
            corner=True
        if self.rect.x > 0:
            self.rect.x=0      
            corner=True     
        if self.rect.y < -(self.y_border):
            self.rect.y=-self.y_border
            corner=True
        if self.rect.y > (0):
            self.rect.y=0
            corner=True
        return corner

    def update(self):
        """ Find a new position for the backround"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.resetspeed()

        self.check_corner()        
    
