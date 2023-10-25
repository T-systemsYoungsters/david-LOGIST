#David Vilhena Klein
# 05.10.2023
# Ein tolles Bild mit Pygame malen
# pygame lab 5, nach http://programarcadegames.com


import pygame, random
pygame.init()
pygame.font.init()

def draw_text(text, size, col, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (50, 168, 82)
GREEN2   = (106, 196, 22)
RED      = (191, 2, 2)
BLUE     = (42, 86, 219)
GREY     = ( 100, 100, 100)
BROWN    = (191, 97, 2)

height=500
widh=700
size = (widh, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Davids tolles Py-Game")

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, [0,0,700,300])
    for xoffset in range(1, widh, 30):
        for yoffset in range(1, height, 30):
            pygame.draw.circle(screen, WHITE, [xoffset+random.randint(-10,10), yoffset+random.randint(-10,10)], 2)
    pygame.draw.rect(screen, GREEN, [0,300,700,500])
    pygame.draw.line(screen, GREY, (0,470), (700,420), 30)
    pygame.draw.rect(screen, RED, [270,250,100,100])
    pygame.draw.polygon(screen, BROWN, [(260,250),(380,250),(320,150)])
    for i in range(285, 360, 20):
        for j in range(260, 320, 35):
            pygame.draw.rect(screen, BLACK, [i,j, 10, 20])
    pygame.draw.circle(screen, BROWN, (320,150),10)
    pygame.draw.circle(screen, BLACK, (320,223),10)
    pygame.draw.rect(screen, BLACK, [310, 325, 20, 25])
    pygame.draw.ellipse(screen, WHITE, [20,20,100,50])
    pygame.draw.ellipse(screen, WHITE, [30,40,120,60])
    draw_text("tolles", 20, BLACK, 60, 30)
    draw_text("Bild", 20, BLACK, 70, 60)
    pygame.draw.rect(screen, BROWN, [280, 190, 10, 30])
    pygame.draw.rect(screen, RED, [400, 400, 150, 30])
    pygame.draw.rect(screen, RED, [430, 380, 90, 50])
    pygame.draw.circle(screen, BLACK, (430,430),20)
    pygame.draw.circle(screen, BLACK, (520,430),20)
    offset =5
    for l in range (280, 340, 20):
        for k in range(15+offset,260, 40):  
            pygame.draw.rect(screen, BROWN, [k, l, 10, 30])
            pygame.draw.circle(screen, GREEN2, (k-3,l),10)
            pygame.draw.circle(screen, GREEN2, (k+9,l+1),10)
            pygame.draw.circle(screen, GREEN2, (k+4,l-5),10)
        for m in range(390+offset,695, 40):
            pygame.draw.rect(screen, BROWN, [m, l, 10, 30])
            pygame.draw.circle(screen, GREEN2, (m-3,l),10)
            pygame.draw.circle(screen, GREEN2, (m+9,l+1),10)
            pygame.draw.circle(screen, GREEN2, (m+4,l-5),10)
        offset=offset*(-1)

    pygame.draw.rect(screen, BROWN, [40, 400, 100, 10])
    pygame.draw.rect(screen, BROWN, [40, 370, 100, 20])
    pygame.draw.rect(screen, BROWN, [60, 390, 10, 20])
    pygame.draw.rect(screen, BROWN, [108, 390, 10, 20])
    pygame.draw.rect(screen, BROWN, [40, 400, 10, 30])
    pygame.draw.rect(screen, BROWN, [130, 400, 10, 30])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(1)

pygame.quit()