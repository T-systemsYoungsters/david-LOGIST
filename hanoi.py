#David Vilhena Klein
#05.10.2022
#Visualisierung der Türme von Hanoi mit Pygame
import pygame
pygame.init()
pygame.font.init()

#color constants
BLACK    = (   0,   0,   0)
GREY     = ( 100, 100, 100)
WHITE    = ( 255, 255, 255)
GREEN    = (  50, 168,  82)
RED      = ( 191,   2,   2)
BLUE     = (  42,  86, 219)
YELLOW   = ( 247, 235,   0)
BROWN    = ( 191,  97,   2)
ROSE     = ( 247,   0, 222)
BRIGHTGREEN = (76, 186, 142)
ORANGE   = ( 186,  129, 76)
CYAN     = (  22,  196, 179)

#settings screen
widh=1000
height=900
size = (widh, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Türme von Hanoi")

# utility function to draw text on screen
def draw_text(text, size, col, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# function that draws every item of a given list on the screen. Here you can define the size and color of the blocks
def drawlist(list, x):
    pos=1 #position in the list/in the column
    for i in list:
        if i==1:
            pygame.draw.rect(screen, GREEN, [x,(9-pos)/10*height,100,50])
        elif i==2:
            pygame.draw.rect(screen, BROWN, [x,(9-pos)/10*height,140,50])
        elif i==3:
            pygame.draw.rect(screen, BLUE, [x,(9-pos)/10*height,180,50])
        elif i==4:
            pygame.draw.rect(screen, RED, [x,(9-pos)/10*height,200,50])
        elif i==5:
            pygame.draw.rect(screen, GREY, [x,(9-pos)/10*height,210,50])
        elif i==6:
            pygame.draw.rect(screen, ROSE, [x,(9-pos)/10*height,220,50])
        elif i==7:
            pygame.draw.rect(screen, BRIGHTGREEN, [x,(9-pos)/10*height,230,50])
        elif i==8:
            pygame.draw.rect(screen, ORANGE, [x,(9-pos)/10*height,240,50])
        elif i==9:
            pygame.draw.rect(screen, CYAN, [x,(9-pos)/10*height,255,50])
        pos+=1

#function that takes a list and returns the the list in moving direction
def firstAttempt(originList): #if amountDisks is even, it is faster to move right, uneven left
    if amountDisks % 2 == 0: # Check if amountDisks is even
        if originList == A:
            return B #output the list to the right
        elif originList == B:
            return C
        elif originList == C:
            return A
    else:
        if originList == A:
            return C
        elif originList == B:
            return A
        elif originList == C:
            return B

#function that returns the list opposite to moving direction (for the second try)
def secondAttempt(originList):
    if amountDisks % 2 != 0: # Check if amountDisks is even
        if originList == A:
            return B #output the list to the right
        elif originList == B:
            return C
        elif originList == C:
            return A
    else:
        if originList == A:
            return C
        elif originList == B:
            return A
        elif originList == C:
            return B

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#I use three lists to keep track of the disks on screen. They work as columns
A=[]
B=[]
C=[]
goal=[] #Checks if C == goal

# function to move one block to another list
def move(block, origin, destination):
    #go through list A, remove desired block and append it to destination but only if the block is smaller
    moved=False
    for i in origin:
        if i==block and ruleCompliance(block, origin, destination) == True: #check ruleCompliance
            origin.remove(block)
            destination.append(i)
            print("moved Block", block)
            moved = True
    return moved

#function to check rule compatability.
def ruleCompliance(block, origin, destination):
    possible=True
    # only the top block can be moved
    if block != origin[len(origin)-1]: #block that should be moved has to match the block on the top of the list
        possible=False
    # if destination list ist not empty, the moved block must be smaller as the block before
    if len(destination) > 0:
        if block > destination[len(destination)-1]:
            possible=False
    return possible

# the amount of Disks can be increased up to 9. For additional disks, define them with a color in drawlist() and tweak the block height
amountDisks = 5
for i in range(amountDisks): #Put Disks into the first list before start
    A.append(amountDisks-i)
    goal.append(amountDisks-i)


# -------- Main Program Loop -----------
iterations=0 # Keep track of our iterations
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            done = True # Exit if user presses a key
    

    # --- Game Logic
    
    if iterations>0: # Wait one iteration before execution
        pygame.time.wait(500) #Wait 1000 miliseconds. Be sure to lower the wait with higher amountDisks
        # Every uneven iteration, move Block 1 one List in moving direction
        if iterations % 2 != 0: 
            if A.count(1)==1: #check if Block 1 is in List A
                move(1, A, firstAttempt(A)) #move Block 1 from List A to list in moving direction
            elif B.count(1)==1:
                move(1, B, firstAttempt(B))
            elif C.count(1)==1:
                move(1, C, firstAttempt(C))
        #every even iteration move the greatest Block possible in moving direction
        else:
            moved=False #to check if Block was moved or not
            checkGreatestBlock=amountDisks #start with the greatest
            while moved==False: #try until some block was moved
                if A.count(checkGreatestBlock) == 1: #if the block is in the first list, do:
                    if move(checkGreatestBlock, A, firstAttempt(A)) != True: # see if block can be moved in moving direction
                        moved=move(checkGreatestBlock, A, secondAttempt(A)) #if not, move in opposite direction
                    else:
                        moved=True #change moved to True if it could be changed in the first attempt
                elif B.count(checkGreatestBlock) == 1:
                    if move(checkGreatestBlock, B, firstAttempt(B)) != True:
                        moved=move(checkGreatestBlock, B, secondAttempt(B))
                    else:
                        moved=True
                elif C.count(checkGreatestBlock) == 1:
                    if move(checkGreatestBlock, C, firstAttempt(C)) != True:
                        moved=move(checkGreatestBlock, C, secondAttempt(C))
                    else:
                        moved=True

                checkGreatestBlock-=1 #check the second greatest block in the next round

    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    #draw columns A,B and C
    draw_text('A', 30, BLACK, widh*2/10, height*9/10) 
    drawlist(A, widh/10)
    draw_text('B', 30, BLACK, widh*5/10, height*9/10)
    drawlist(B, widh*4/10)
    draw_text('C', 30, BLACK, widh*8/10, height*9/10)
    drawlist(C, widh*7/10)
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)# Limit to 60 frames per second
    
    iterations+=1

    if C == goal: # exit if goal is reached
        print("Finished in {} steps.".format(iterations-1))
        pygame.time.wait(1000) #wait for 1000 miliseconds
        done=True
    

pygame.quit()