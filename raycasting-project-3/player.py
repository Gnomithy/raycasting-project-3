from math import sin, cos, tau
import pygame as pg
from settings import *
from sys import exit

class Player(pg.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.width = self.height = 15
        self.image = pg.Surface([self.width, self.height])
        self.game = game
        self.x, self.y = START_POS
        self.angle = START_ANGLE
        self.rect = self.image.get_rect()
    
    def movement(self):
        sinA = sin(self.angle)
        cosA = cos(self.angle)
        dx, dy = 0, 0 
        speed = PLAYER_SPEED * self.game.delta_time
        speed_cos = speed * cosA
        speed_sin = speed * sinA


        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        
        # if keys[pg.K_a]:
        #     dx += speed_cos
        #     dy += -speed_sin
        
        # if keys[pg.K_d]:
        #     dx += -speed_cos
        #     dy += speed_sin

        self.check_collision(dx, dy)

        if keys[pg.K_a]:
            self.angle -= ROTATIONAL_SPEED * self.game.delta_time

        if keys[pg.K_d]:
            self.angle += ROTATIONAL_SPEED * self.game.delta_time

        self.angle %= tau
    
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map


    def check_collision(self, dx, dy):
        scale = SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        elif not self.check_wall(int(self.x + dx * scale), int(self.y)):
            if self.game.map.world_map[(int(self.x + dx * scale),int(self.y))] == 2:
                pg.quit()
                exit()
            # elif self.game.map.world_map[(int(self.x + dx * scale),int(self.y))] == 3:
                
            
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
        elif not self.check_wall(int(self.x), int(self.y + dy * scale)):
            if self.game.map.world_map[(int(self.x), int(self.y + dy * scale))] == 2:
                pg.quit()
                exit()
        
    
        # def coin_collection(self):
        #     for i in range(self.x - 10, self.x + 10):
        #         for j in range(self.y - 10, self.y + 10):
        #             if (i, j) == self.game.sprite.start_pos:
                    
    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * BOX_SIZE, self.y * BOX_SIZE),
                     (self.x * BOX_SIZE + 150 * cos(self.angle),
                      self.y * BOX_SIZE + 150 * sin(self.angle)), 5)
        pg.draw.circle(self.game.screen, 'red', (self.x * BOX_SIZE, self.y * BOX_SIZE), 15)

    def update(self):
        self.movement()
        self.rect.center = self.x, self.y

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)