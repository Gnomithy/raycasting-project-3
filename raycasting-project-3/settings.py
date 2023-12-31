from math import pi, tan 

WIDTH = 800
HEIGHT = 450
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 0
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2


START_POS = 2, 2
START_ANGLE = 0
PLAYER_SPEED = 0.003
ROTATIONAL_SPEED = 0.0015
SIZE_SCALE = 60



BOX_SIZE = 50

WINNING_SQUARE = (5, 6)
FOV = pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
ANGLE_INC = FOV / NUM_RAYS
MAX_DEPTH = 20
SCREEN_DIST = HALF_WIDTH / tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS


TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2


SPRITE_POS = {
    'coin':[(125, 125), (425, 175), (225, 325)]
}
