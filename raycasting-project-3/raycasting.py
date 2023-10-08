from math import sin, cos, tau, pi
import pygame as pg

from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            wall_depth, proj_height, texture, offset = values

            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(
                offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)
                
            self.objects_to_render.append((wall_depth, wall_column, wall_pos))
    def ray_cast(self):
        self.ray_casting_result = []
        player_x, player_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        

        v_texture, h_texture = 1, 1
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sinA = sin(ray_angle)
            cosA = cos(ray_angle)


            # if self.game.player.angle <= ((tau / 4) * 3) and self.game.player.angle >= (pi / 2):
            #     self.game.map.map[WINNING_SQUARE[1]][WINNING_SQUARE[0]] = 1
            #     print(self.game.map.map[WINNING_SQUARE[1]][WINNING_SQUARE[0]])
        
            # else:
            #     self.game.map.map[WINNING_SQUARE[1]][WINNING_SQUARE[0]] = 2

            
            hy, dy = (map_y + 1, 1) if sinA > 0 else (map_y - 1e-6, -1)

            h_mag = (hy - player_y) / sinA
            hx = player_x + h_mag * cosA

            d_mag = dy / sinA
            dx = d_mag * cosA

            for i in range(MAX_DEPTH):
                x_tile = int(hx), int(hy)
                if x_tile in self.game.map.world_map:
                    h_texture = self.game.map.world_map[x_tile]
                    break
                hx += dx
                hy += dy
                h_mag += d_mag
            
            vx, dx = (map_x + 1, 1) if cosA > 0 else (map_x - 1e-6, -1)

            v_mag = (vx - player_x) / cosA
            vy = player_y + v_mag * sinA

            d_mag = dx / cosA
            dy = d_mag * sinA

            for i in range(MAX_DEPTH):
                y_tile = int(vx), int(vy)
                if y_tile in self.game.map.world_map:
                    v_texture = self.game.map.world_map[y_tile]
                    break
                vx += dx
                vy += dy
                v_mag += d_mag

            if v_mag > h_mag:
                wall_depth, texture  = h_mag, h_texture
                hx %= 1
                offset = hx if sinA > 0 else (1 - hx)
            else:
                wall_depth, texture = v_mag, v_texture 
                vy %= 1
                offset = vy if cosA > 0 else(1 - vy)

            wall_depth *= cos(self.game.player.angle - ray_angle)

            proj_height = SCREEN_DIST / (wall_depth + 0.0001)

            color = ((200 / (1 + wall_depth ** 7 * 0.00002)), 0, (255 / (1 + wall_depth ** 7 * 0.00002)))
            self.ray_casting_result.append((wall_depth, proj_height, texture, offset))
            pg.draw.rect(self.game.screen, color, 
                        (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))


            ray_angle += ANGLE_INC

    def update(self):
        self.ray_cast()
        self.get_objects_to_render()

# ((tau * 3) / 4) <= self.game.player.angle <= (tau / 4)           