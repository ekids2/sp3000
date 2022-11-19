from sys import exit
from pygame.locals import *
from GameSpaceships import *
import random

# Ініціалізація всіх допоміжних команд з модуля PYGAME
pygame.init()

# Задати розміри екрану нашої гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Назва нашої гри
pygame.display.set_caption("Space Invader 3000")

# Завантажити малюнок, який буде фоном у нашій грі
GAME_BACKGROUND = pygame.image.load('resources/background.png').convert()

# Завантажити музику, яка буде грати у нашій грі
pygame.mixer.music.load('resources/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# Вказуємо шлях до малюнка, в якому є різні моделі космічних кораблів
filename = 'resources/aircraft_shooter.png'

# Створюємо змінну в якій будемо зберігати завантажений у нашу гру цей малюнок
spaceship_images = pygame.image.load(filename)

# Створюємо змінну типу масив, в якій створюємо обʼєкти прямокутникі згідно з координатами у малюнку
challenger_images = [pygame.Rect(0, 99, 102, 126), pygame.Rect(165, 360, 102, 126), pygame.Rect(165, 234, 102, 126),
                     pygame.Rect(330, 624, 102, 126), pygame.Rect(330, 498, 102, 126), pygame.Rect(432, 624, 102, 126)]

# Створюємо змінну типу лист, в якій будемо зберігати координати
challenger_position = [200, 600]

# Створюємо змінну, обʼєкт нашого космічного корабля, за допомогою якої будемо керувати й видозмінювати наш корабель
challenger = Challenger(spaceship_images, challenger_images, challenger_position)

# Створюємо змінну, обʼєкт куль, які використовує нашог космічний корабель
challenger_bullet = pygame.Rect(1004, 987, 9, 21)
bullet_images = spaceship_images.subsurface(challenger_bullet)

# Створюємо змінну, обʼєкт наших ворогів, які будуть летіти нам назустріч
enemy = pygame.Rect(534, 612, 57, 43)
enemy_images = spaceship_images.subsurface(enemy)
enemy_down_images = [spaceship_images.subsurface(pygame.Rect(267, 347, 57, 43)),
                     spaceship_images.subsurface(pygame.Rect(873, 697, 57, 43)),
                     spaceship_images.subsurface(pygame.Rect(267, 296, 57, 43)),
                     spaceship_images.subsurface(pygame.Rect(930, 697, 57, 43))]

enemies = pygame.sprite.Group()

# Створюємо змінну, група для того, щоб надалі зберігати наші кораблі які знищені для подальшої анімації
# enemies_down = pygame.sprite.Group()

# Іконка нашої програми
filename = 'resources/ufo.png'
ufo = pygame.image.load(filename)

# Сказати модулю PYGAME, що ми хочемо встановити іконку для нашої гри яку буде видно у "пуску" або у верхньому куті
# самої програми, тобто нашої гри
pygame.display.set_icon(ufo)

# Нам потрібно контролювати ФПС у грі, тож ми створюємо змінні, які надалі будемо використовувати для задання ФПС
# саме у грі
CLOCK = pygame.time.Clock()
FPS = 60  # Frames per second.

# Блок змінних які необхідні для визначення дистанції ворогів від краю екрану, кулі, й нашого корабля
shot_distance = 0
# enemy_distance = 0
# challenger_down_index = 16
# challenger_distance = 0

running = True
while running:

    # Контролю у грі ФПС
    CLOCK.tick(FPS)

    # Не заповнюємо наш екран нічим, бо в нас є фоновий малюнок
    screen.fill((0, 0, 0))

    # Встановлюємо фоновий малюнок
    screen.blit(GAME_BACKGROUND, (0, 0))

    # Малюємо кулі які летять з певною швидкістю й міняють дистанцію
    #if not challenger.is_hit:
    #    if shot_distance % 15 == 0:
    #        challenger.shoot(bullet_images)
    #    shot_distance += 1
    #    if shot_distance >= 15:
    #        shot_distance = 0

    # Генеруємо наших ворогів
    if shot_distance % 50 == 0:
        enemy_position = [random.randint(0, SCREEN_WIDTH - enemy.width), 0]
        enemy_ship = EnemyShip(enemy_images, enemy_down_images, enemy_position)
        enemies.add(enemy_ship)
    # enemy_distance += 1
    # if enemy_distance >= 100:
    #     enemy_distance = 0

    # Рухаємо кулі від корабля просто вгору
    # for bullet in challenger.bullets:
    #     bullet.move()
    #     if bullet.rect.bottom < 0:
    #         challenger.bullets.remove(bullet)

    # Використовуємо цикл, й вказуємо, щоб всі кораблі прибульці почали рухатись
    for enemy_ in enemies:
        enemy_.move()
        # Додаємо умову, що якщо корабель й вороже нло зіштовхуються, то нло - зникає
        # Або зникає наш корабель
        # if pygame.sprite.collide_circle(enemy_, challenger):
        #     enemies_down.add(enemy_)
        #     enemies.remove(enemy_)
        #     challenger.is_hit = True
        #     break
        # if enemy_.rect.top > SCREEN_HEIGHT:
        #     enemies.remove(enemy_)

    # Створюємо змінну, яка буде слідкувати за збиттям ворожих кораблів
    # А також, створюємо цикл, за допомогою якого будемо слідкувати, що для кожного згенерованого ворожого
    # корабля є умова його "зникання"
    # enemies_down_ = pygame.sprite.groupcollide(enemies, challenger.bullets, 1, 1)
    # for enemies_ in enemies_down_:
    #     enemies_down.add(enemies_)

    # Створюємо блок коду - умову за допомогою якої питаємо у програми яку подію наразі обрав користувач
    # Якщо це подія - вийти з програми - ми успішно виходимо
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Малюємо наш космічний корабель, але з умовою, що, якщо в нього поцілили, мусимо його "прибрати" з екрану
    # if not challenger.is_hit:
    #     screen.blit(challenger.image[challenger.img_index], challenger.rect)
    #     # Змінюємо індекс зображення, щоб зробити літак анімованим
    #     challenger.img_index = shot_distance // 8
    # else:
    #     challenger.img_index = challenger_down_index // 8
    #     screen.blit(challenger.image[challenger.img_index], challenger.rect)
    #     challenger_down_index += 1
    #     if challenger_down_index > 47:
    #         running = False

    # Створюємо змінну, в якій будемо зберігати масив клавіш, які може натиснути користувач з клавіатури
    key_pressed = pygame.key.get_pressed()

    # Перевіряємо, що саме натиснув користувач
    # Користувач може користуватись WASD чи стрілками, ми обробляємо цю подію й керуємо нашим космічним кораблем
    # у відповідності натискання на клавіші, що натискає користувач, будемо рухати корабель
    if key_pressed[K_w] or key_pressed[K_UP]:
        challenger.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        challenger.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        challenger.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        challenger.moveRight()

    # Малюємо на нашому екрані гри кулю, яка прикріплена до нашого космічного корабля
    # Прибираємо постріл кулі, бо ми це зробили вище
    challenger.shoot(bullet_images)
    challenger.bullets.draw(screen)

    # Малюємо на екрані кораблі суперників
    enemies.draw(screen)

    # Малюємо наш космічний корабель на екрані гри
    # Прибираємо малювання корабля, бо ми його намалювали вище
    screen.blit(challenger.image[challenger.img_index], challenger.rect)

    # Оновлюємо наш екран
    pygame.display.update()
