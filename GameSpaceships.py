import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# Створення інструкції до обʼєкту типу Куля (те чим буде стріляти наш космічний корабель)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_images, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_images
        self.rect = self.image.get_rect()
        self.rect.midbottom = initial_position
        self.speed = 10

    # Додаємо функцію яка буде за рух кулі, якими стріляє наш космічний корабель
    def move(self):
        self.rect.top -= self.speed


# Створення інструкції до обʼєкту типу Челенджер (космічний корабель)
class Challenger(pygame.sprite.Sprite):
    def __init__(self, spaceships_images, challenger_images, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        for i in range(len(challenger_images)):
            self.image.append(spaceships_images.subsurface(challenger_images[i]).convert_alpha())
        self.rect = challenger_images[0]
        self.rect.topleft = initial_position
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    # Додаємо нову функцію яка буде відповідати за кулі, якими стріляє наш космічний корабель
    def shoot(self, bullet_images):
        bullet = Bullet(bullet_images, self.rect.midtop)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


# Створення інструкції до обʼєкту типу ворожий корабель
class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, opponent_resource, opponent_down_resources, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = opponent_resource
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = opponent_down_resources
        self.speed = 2
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed
