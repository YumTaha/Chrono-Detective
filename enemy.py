import pygame

WIDTH = 800
HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, max_health=50):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red color for enemy
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 3

        self.max_health = max_health
        self.health = max_health

    def move(self, player_pos):
        # Move toward the player
        self.direction = player_pos - self.pos
        if self.direction.magnitude() > 0: 
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

        # Border collision detection
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, player_pos, *args, **kwargs):
        self.move(player_pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()


