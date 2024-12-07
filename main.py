import pygame
from constants import *
from player import *

def main():
    #delta-time: amount of time between each frame
    dt = 0

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    while True:

        # Close the window with the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)
        screen.fill("black")
        for i in drawable:   
            i.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000








if __name__ == "__main__":
    main()
    