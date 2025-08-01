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
racket1 = Player('racket.png', 30, 200, 20, 80, 5)
racket2 = Player('racket.png', 540, 200, 20, 80, 5)
ball = GameSprite('tenis_ball.png', 200, 200, 40, 40, 50)

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
    if finish != True:
        window.fill(bg)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loose1, (200, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(loose2, (200 ,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)
