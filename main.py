import pygame
import player
import asteroid
import asteroidfield
import shot
from constants import *




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    c = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)

    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    f = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = c.tick(60)/1000
        
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        

        for a in asteroids:
            if p.colliding(a):
                print("Game over!")
                exit()
            
            for s in shots:
                if a.colliding(s):
                    a.split()
                    s.kill()
            
        print(shots)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
