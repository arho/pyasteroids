import pygame
import player

from constants import *




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    c = pygame.time.Clock()
    dt = 0
    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = c.tick(60)/1000        
        p.update(dt)
        p.draw(screen)


        pygame.display.flip()
        

if __name__ == "__main__":
    main()
