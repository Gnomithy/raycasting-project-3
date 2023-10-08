from sys import exit
import pygame as pg
from settings import *
from map import Map
from player import Player
from raycasting import Raycasting
from object_renderer import ObjectRenderer
from sprite import Sprite

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.game_time = pg.time.Clock()
        self.delta_time = 1
        self.font = pg.font.SysFont('calibri', 16)
        self.new_game()

    def new_game(self):
        global  coins
        coins = []
        self.player = Player(self)
        self.map = Map(self)
        self.coin = Sprite(self)
        coins.append(self.coin)
        self.object_renderer = ObjectRenderer(self)
        # self.raycasting = Raycasting(self)

    def update(self):
        self.player.update()
        # self.raycasting.update()
        # self.map.check_angle()
        for i in range(len(coins)):
           if pg.Rect.colliderect(self.player.rect, coins[i].rect):
               del coins[i]
        self.delta_time = self.game_time.tick(FPS) + 0.0001
        pg.display.update()
        pg.display.flip()
        

    def draw(self):
        self.screen.fill('black')
        # self.object_renderer.draw()
        self.map.draw()
        for coin in coins:
            coin.draw()
        self.player.draw()
        # self.coin.draw()
    
    def event_checker(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        



        
    def run(self):
        while True:
            self.event_checker()
            self.update()
            self.draw()
