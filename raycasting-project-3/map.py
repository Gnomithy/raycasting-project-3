import pygame as pg
from settings import BOX_SIZE, WINNING_SQUARE
from math import sin, cos

class Map:
    def __init__(self, game):
        global map
        self.game = game
        self.angle = game.player.angle
        self.world_map = {}
        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                    [1,0,0,1,0,0,0,0,0,0,3,0,0,0,0,1],
                    [1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1],
                    [1,0,1,1,0,0,2,0,0,0,0,0,0,0,0,1],
                    [1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],    
                    ]
        self.get_map()
    def get_map(self):
        

        for i, row in enumerate(self.map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j, i)] = value
        
    def draw(self):
            colour = (100, 100, 100)
            for pos in self.world_map:
                if self.map[pos[1]][pos[0]] == 3:
                    pg.draw.rect(self.game.screen, 'blue',  (pos[0] * BOX_SIZE, pos[1] * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                else:
                    pg.draw.rect(self.game.screen, colour,  (pos[0] * BOX_SIZE, pos[1] * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                        
    def check_angle(self):
        if (sin(self.angle) > 0 and cos(self.angle) > 0) or (sin(self.angle) < 0 and cos(self.angle > 0)) or self.angle == 0:
            self.map[WINNING_SQUARE[0]][WINNING_SQUARE[1]] = 2
        
        else:
            self.map[WINNING_SQUARE[0]][WINNING_SQUARE[1]] = 1


