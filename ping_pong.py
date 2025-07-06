from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

#Создаю игровую сцену

bg = (200,200,255)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(bg)

# Флаги, отвечающие за состояние игры

clock = time.Clock()
FPS = 60
game = True
finish = False

# Создание мяча и ракетки
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 30, 520, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
loose1 = font.render('Player 1 loose', True, (180, 0, 0))
loose2 = font.render('Player 2 loose', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
