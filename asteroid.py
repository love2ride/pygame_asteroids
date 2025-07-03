import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()  # Wird im main.py gesetzt

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (200, 200, 200), self.position, self.radius, 2)