import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    containers = tuple()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y),self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        fragment_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        fragment_one.velocity = self.velocity.rotate(angle)
        fragment_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        fragment_two.velocity = self.velocity.rotate(-angle)
        fragment_two.velocity.rotate(-angle)
