import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta-Zeit initialisieren
    
    # Gruppen für update und draw
    updatables = pygame.sprite.Group() 
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    # Setze die containers für Asteroid und AsteroidField
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    
    # 🧍‍♂️ Player in der Mitte des Bildschirms erzeugen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, radius=20, player_radius=10)
    # Füge den Spieler zu den Gruppen hinzu
    updatables.add(player)
    drawables.add(player)
    
    
    # AsteroidField erzeugen
    asteroid_field = AsteroidField()
    
    while True:
        # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Alle Objekte updaten
        for obj in updatables:
            obj.update(dt)
        
        # Kollisionen prüfen
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
        
        # Kollisionen prüfen: Schüsse vs. Asteroiden
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()
                    
        # Bildschirm schwarz füllen
        screen.fill((0, 0, 0))
        
        # Alle Objekte zeichnen
        for obj in drawables:
            obj.draw(screen)
        
        # Anzeige aktualisieren
        pygame.display.flip()
        
        # Framerate begrenzen und Delta-Zeit berechnen
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()