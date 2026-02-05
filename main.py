import pygame
import sys
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TWILIGHT_BG, DEATH_MESSAGES
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 

def main():
    pygame.init()
    pygame.display.set_caption("Bastroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(x, y)

    #1. Handle Inputs (Events)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #2. Update (Game Logic)
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print(random.choice(DEATH_MESSAGES))
                return

        for asteroid in list(asteroids):
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        screen.fill(TWILIGHT_BG)

        #3. Draw (Rendering)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #4. Tick the Clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
