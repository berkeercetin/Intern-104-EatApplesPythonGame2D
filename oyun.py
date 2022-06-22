import pygame
import random

pygame.init()

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))

class Apple(pygame.sprite.Sprite):

    def __init__(self,posY):
        super().__init__()

        self.sizeX = 40
        self.sizeY = 40

        self.posX = random.randint(0,window_width - self.sizeX)
        self.posY = posY

        self.apple = pygame.image.load("requirement/apple.png")
        self.apple = pygame.transform.scale(self.apple, (self.sizeX, self.sizeY))

        self.rect = self.apple.get_rect()
        self.rect.center=[self.posX,self.posY]

    def MoveApple(self):
        self.posY += 8

        if self.posY > window_height:
            self.posY = 0 - self.sizeY

class Core(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        pygame.display.set_caption("elmaları ye")
        self.clock = pygame.time.Clock()

        self.sizeX = 150
        self.sizeY = 150

        self.enemy = pygame.image.load("requirement/apple.png")
        self.player = pygame.image.load("requirement/alya.png")
        self.player = pygame.transform.scale(self.player, (self.sizeX, self.sizeY))

        self.background = pygame.image.load("requirement/background.png")


        self.player_x = 500
        self.player_y = 500

        self.enemy_x=500
        self.enemy_y=200

        self.moveRight = False
        self.moveLeft = False

        self.rect = self.player.get_rect()
        self.rect.center=[self.player_x,self.player_y]

    def Move(self):
        if self.moveRight:
            self.player_x += 15
        if self.moveLeft:
            self.player_x -= 15


    def draw(self):

        window.blit(self.background, (0, 0))
        #self.window.blit(self.enemy, (self.enemy_x, self.enemy_y))
        window.blit(self.player, (self.player_x, self.player_y))

        window.blit(apple.apple,(apple.posX, apple.posY))

        self.clock.tick(60)
        pygame.display.update()

    def WhoEatApple(self):
        if apple.posX > self.player_x and apple.posX < self.player_x + self.sizeX and apple.posY > self.player_y:
            apple.posY = 0 - apple.sizeY
            apple.posX = random.randint(0, window_width - self.sizeX)

    def game_loop(self):
        self.WhoEatApple()
        apple.MoveApple()

        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.moveRight = True
                if event.key == pygame.K_a:
                    self.moveLeft = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.moveRight = False
                if event.key == pygame.K_a:
                    self.moveLeft = False


        if self.keys[pygame.K_ESCAPE]:
            return 0

        self.draw()
        self.Move()

game = Core()
apple = Apple(-30)

while True:
    game_status = game.game_loop()
    if game_status is not None:
        break

pygame.quit()