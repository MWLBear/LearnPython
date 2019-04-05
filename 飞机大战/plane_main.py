import pygame
from plane_sprites import *

class PlaneGame(object):
    #飞机大战主游戏
    def __init__(self):
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCFEEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        print("init game...")
        # 创建私有方法,精灵和精灵组的创建
        self.__creat_sprites()
        # 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREAT_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def __creat_sprites(self):
        # 背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("start game...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__clock_collide()
            # 更新绘制精灵
            self.__upade_sprites()
            # 更新显示
            pygame.display.update()


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 键盘按键获取
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print
        # 获取键盘按键 - 按键元祖


    def __clock_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()
    def __upade_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over...")
        pygame.quit()
        exit()

if __name__ == '__main__':
    PlaneGame().start_game()
