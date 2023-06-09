import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, max_health=100):
        super().__init__()
        self.X = 50; self.Y = 50
        self.image = pygame.Surface((self.X, self.Y))
        self.image.fill((255, 255, 0))  # Yellow color for player
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 5

        self.max_health = max_health
        self.health = max_health
        self.score = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self):
        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # print(self.direction)
        # horizontal movement
        self.pos.x += self.direction.x * self.speed
        if self.pos.x < (self.X // 2):
            self.pos.x = (self.X // 2)
        elif self.pos.x > WIDTH - (self.X // 2):
            self.pos.x = WIDTH - (self.X // 2)
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed
        if self.pos.y < (self.Y // 2):
            self.pos.y = (self.Y // 2)
        elif self.pos.y > HEIGHT - (self.Y // 2):
            self.pos.y = HEIGHT - (self.Y // 2)
        self.rect.centery = self.pos.y

    def update(self, *args, **kwargs):
        self.input()
        self.move()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()