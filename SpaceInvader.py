import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Цей блок коду нам уже не потрібен, бо ми замість заливки будемо використовувати малюнок
# То цей блок коду можемо сміло видалити
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ініціалізація всих допоміжних команд з модулю PYGAME
pygame.init()

# Задати розміри екрану нашої гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Назва нашої гри
pygame.display.set_caption('Space Invader 3000')

# Завантажити малюнок, який буде фоном у нашій грі
GAME_BACKGROUND = pygame.image.load('resources/background.png').convert()

# Іконка нашої програми
filename = 'resources/ufo.png'
ufo = pygame.image.load(filename)

# Сказати модулю PYGAME, що ми хочемо встановити ворогів на екрані
pygame.display.set_icon(ufo)

# Створення нашого Спейс Інвайдера, й вказання на яких координатах він буде розташований
AIRCRAFT_PLAYER_IMG = pygame.image.load('resources/spaceship.1.png')
AIRCRAFT_POSITION_X = 370
AIRCRAFT_POSITION_Y = 480
AIRCRAFT_POSITION_X_CHANGE = 0


def player(x, y):
    screen.blit(AIRCRAFT_PLAYER_IMG, (x, y))


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(GAME_BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                AIRCRAFT_POSITION_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                AIRCRAFT_POSITION_X_CHANGE = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                AIRCRAFT_POSITION_X_CHANGE = 0

    AIRCRAFT_POSITION_X += AIRCRAFT_POSITION_X_CHANGE
    if AIRCRAFT_POSITION_X <= 0:
        AIRCRAFT_POSITION_X = 0
    elif AIRCRAFT_POSITION_X >= 736:
        AIRCRAFT_POSITION_X = 736

    player(AIRCRAFT_POSITION_X, AIRCRAFT_POSITION_Y)
    pygame.display.update()
