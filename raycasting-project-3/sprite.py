import pygame as pg
from settings import *
from random import choice

class Sprite(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.width = self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.image.fill((0, 0, 255))
        self.name = 'coin'
        self.start_pos = (0,0)
        self.get_start_pos()
        self.rect = self.image.get_rect(center = self.start_pos)
        
    def get_start_pos(self):
        self.start_pos = choice(SPRITE_POS[self.name])
    
    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (self.start_pos), 5)

    
