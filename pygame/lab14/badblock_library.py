import pygame, random
from block_library import *

class Badblock(Block):
    def __init__(self, width, height):
        super().__init__(( 255, 0,  0), width, height)
    def update(self):
        self.rect.y+=1
        if self.rect.y > 380:
            self.rect.x=random.randint(0,700)
            self.rect.y=random.randint(-420,-20)