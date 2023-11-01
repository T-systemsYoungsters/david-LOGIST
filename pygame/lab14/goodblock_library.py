from typing import Any
import pygame, random
from block_library import *

class GoodBlock(Block):
    def __init__(self, width, height):
        super().__init__(( 51, 204,  51), width, height)

    def update(self):
        self.rect.x+=random.randint(-3,3)
        self.rect.y+=random.randint(-3,3)