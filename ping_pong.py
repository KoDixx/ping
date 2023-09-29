from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pl_img, x,y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pi_img), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed  

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed  

window = display.set_mode((700,500))
display.set_caption('ping-pong')
bacbackground = transform.scale(image.load('fon.jpg'),(700,500))

clock = time.Clock()
FPS = 60

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(bacbackground, (0,0))

    display.update()
    clock.tick(FPS)                   
