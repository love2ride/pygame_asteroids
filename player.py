from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y, radius, player_radius):
        super().__init__(x, y, radius)
        self.player_radius = player_radius
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
        
    def update(self, dt):
        # Timer verringern
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)  # Links drehen
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)   # Rechts drehen
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:  # Überprüfen, ob der Schuss erlaubt ist
                self.timer = PLAYER_SHOOT_COOLDOWN
                self.shoot()
        self.move(dt)
            
    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_UP]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_DOWN]:
            self.position -= forward * PLAYER_SPEED * dt
            
    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)