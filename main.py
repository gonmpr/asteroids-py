import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():

    #delta-time: amount of time between each frame
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #Groups definitions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

    #Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_spawn_field = AsteroidField()


    while True:

        # Close the window with the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)


        for asteroid in asteroids:
            if player.in_collision(asteroid):
                print("game over!")
                sys.exit()
        

            for bullet in bullets:
                if asteroid.in_collision(bullet):
                    asteroid.split()
                    bullet.kill()


        screen.fill("black")
        for obj in drawable:   
            obj.draw(screen)
        pygame.display.flip()

        # limits the framerate to 60fps
        dt = clock.tick(60)/1000








if __name__ == "__main__":
    main()
    