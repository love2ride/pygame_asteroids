import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta-Zeit initialisieren
    
    # 🧍‍♂️ Player in der Mitte des Bildschirms erzeugen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, radius=20, player_radius=10)

    while True:
        # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Bildschirm schwarz füllen
        screen.fill((0, 0, 0))
        
         # 🎮 Spieler zeichnen
        player.draw(screen)
        
        # Anzeige aktualisieren
        pygame.display.flip()
        
        # Framerate begrenzen und Delta-Zeit berechnen
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()