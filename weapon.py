import pygame

WIDTH = 800
HEIGHT = 600

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, damage):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((55, 0, 0)) # grey color for weapon
        self.rect = self.image.get_rect(center = (x,y))
        self.damage = damage

    def update(self, *args, **kwargs):

        # Border collision detection
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
    
    def kill(self):
        self.kill()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
