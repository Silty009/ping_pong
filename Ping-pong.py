from pygame import *
from random import randint
from time import time as tm

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
background = transform.scale(image.load('cat_window.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, w, h, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self): #управление игроком
        keys = key.get_pressed()
        
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        






hero = Player(80, 80, 'cat1.png', 620, 250, 4)
hero2 = Player(80, 80, 'cat2.png', 0, 250, 4)
meat = GameSprite(50, 50, 'meat.png', 300, 200, 0)


# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.set_volume(0.3)
# mixer.music.play()
# fire_ = mixer.Sound('fire.ogg')



font.init()
font1 = font.SysFont('Arial', 70)
win = font1.render('YOU WIN!', True, (225, 215, 0))


lose = font1.render('YOU LOSE!', True, (225, 215, 0))

font2 = font.SysFont('Arial', 25) #обязательно заменить класс font на SysFontfont2 = font.SysFont('Arial', 25) 

rel = font2.render('Ждите, перезарядка!', True, (255, 0, 0))

game = True
clock = time.Clock() #создаем игровой таймер



finish = False

while game:
    for e in event.get():#для каждого события в списке событий совершаемый пользователем

        if e.type == QUIT:#если тип события равен нажатому крестику (выходу из игры)

            game = False
    if finish != True:
    
        window.blit(background, (0, 0))
        hero.reset()
        hero2.reset()
        hero.update2()
        hero2.update1()
        meat.reset()



    
    

    
    
    
    
       

    
    
    display.update()
    clock.tick(60)
