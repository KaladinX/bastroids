import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #1. Handle Inputs (Events)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #2. Update (Game Logic)
        player.update(dt)

        #3. Draw (Rendering)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        #4. Tick the Clock
        dt = clock.tick(60) / 1000

        log_state()

if __name__ == "__main__":
    main()
