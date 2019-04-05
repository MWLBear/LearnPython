import random
import pygame

SCFEEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
# 敌机定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 游戏精灵
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):

    # 游戏精灵
    def __init__(self,image_name,speed = 1):
        # 父类的初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

# 游戏背景精灵
class Background(GameSprite):
    def __init__(self,is_alt = False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCFEEN_RECT.height:
            self.rect.y = -SCFEEN_RECT.height

# 敌人飞机精灵
class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1,5)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCFEEN_RECT.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCFEEN_RECT.height:
            self.kill()
    def __del__(self):
        pass
        # print('del %s'%self.rect)

# 英雄精灵
class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCFEEN_RECT.centerx
        self.rect.bottom = SCFEEN_RECT.bottom - 120

        # 子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_RIGHT]:
            self.rect.x += 5
        elif keys_press[pygame.K_LEFT]:
            self.rect.x += -5
        elif keys_press[pygame.K_UP]:
            self.rect.y -= 5
        elif keys_press[pygame.K_DOWN]:
            self.rect.y += 5
        else:
            self.speed = 0
            self.rect.x += self.speed

        if self.rect.right >= SCFEEN_RECT.right:
            self.rect.right = SCFEEN_RECT.right
        elif self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom >= SCFEEN_RECT.bottom:
            self.rect.bottom = SCFEEN_RECT.bottom



    def fire(self):

        for i in (0,1,2,3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

#子弹精灵
class Bullet(GameSprite):

    def __init__(self):

        super().__init__("./images/bullet1.png", -2)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁")
        pass