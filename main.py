import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #global variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #asteroids
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, drawable, updatable)
    spawn_asteroids = AsteroidField()

    #player
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #shots
    Shot.containers = (shots, drawable, updatable)


    #game loop
    while True:
       log_state()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return


       screen.fill("black")

       updatable.update(dt) #read inputs, update state

       for obj in asteroids:
           if obj.collides_with(player):
               log_event("player_hit")
               print("Game Over!")
               sys.exit()


           for shot in shots:
               if shot.collides_with(obj):
                   log_event("asteroid_shot")
                   shot.kill()
                   obj.split()



       for obj in drawable: #render images
          obj.draw(screen)

       pygame.display.flip()
       dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
