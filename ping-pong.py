from pygame import *

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
