from typing import Any
from pygame import *

init()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

MAP_WIDTH, MAP_HEIGHT = 24, 20

TILESIZE = 35
WIDTH, HEIGHT = MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE


window = display.set_mode((WIDTH,HEIGHT))
FPS = 90
clock = time.Clock()

bg = image.load('background.jpg')
bg = transform.scale(bg,(1100,750))
hero_img = image.load('hero.png')
cyborg_img = image.load('cyborg.png')
treasure_img = image.load('treasure.png')
wall_img = image.load('wall.png')


all_sprites = sprite.Group()
class Sprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)

class Player(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.hp = 100
        self.speed = 4


    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if key_pressed[K_a]and self.rect.x >0:
            self.rect.x -= self.speed
        if key_pressed[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_d] and self.rect.right <WIDTH:
            self.rect.x += self.speed
        
        


    



Player = Player(hero_img, TILESIZE , TILESIZE , 300 , 300)
walls = sprite.Group()

with open("map.txt", 'r') as f:
    map = f.readlines()
    x = 0
    y = 0
    for line in map:
        for symbol in line:
            if symbol =="w":
                walls.add(Sprite(wall_img, TILESIZE, TILESIZE, x, y))
            if symbol =="p":
                Player.rect.x=x
                Player.rect.y=y
            x += TILESIZE
        y+= TILESIZE
        x = 0
                


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg,(0,0))
    all_sprites.draw(window)
    all_sprites.update()
   
    
    display.update()
    clock.tick(FPS)


