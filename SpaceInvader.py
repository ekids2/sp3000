import pygame

# Initialize a block with constants for our game window
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Initialization of colors that we need later for filling, for example, the background of the screen and the object
# with which we will work
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize all imported pygame modules
pygame.init()

# Initialize a window or screen for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Let's name our window so that it is clear what game it is
pygame.display.set_caption("Space Invader 3000")

# Let's create an object, a rectangle, with coordinates where it will be placed when opening our game
rect = pygame.Rect((0, 0), (32, 32))

# And also we need to create something that will be in our object, that is our future icon of our Space Invader 3000
image = pygame.Surface((32, 32))

# For a simple example and to learn better of the material, we can simply fill it with white color, which we have
# already created before
image.fill(WHITE)

# Also we can control the FPS in our game, for that let's do the following -
CLOCK = pygame.time.Clock()
FPS = 60  # Frames per second.

RUNNING = True

while RUNNING:
    # Control the maximum frame rate of the game is 60
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         rect.move_ip(0, -2)
        #     elif event.key == pygame.K_DOWN:
        #         rect.move_ip(0, 2)
        #     elif event.key == pygame.K_LEFT:
        #         rect.move_ip(-2, 0)
        #     elif event.key == pygame.K_RIGHT:
        #         rect.move_ip(2, 0)

        screen.fill(BLACK)
        screen.blit(image, rect)
        pygame.display.update()  # Or pygame.display.flip()
