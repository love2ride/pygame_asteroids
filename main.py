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

    # Gruppen für update und draw
    updatables = []
    drawables = []
    
    # Füge den Spieler zu den Gruppen hinzu
    updatables.append(player)
    drawables.append(player)
    
    while True:
        # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Alle Objekte updaten
        for obj in updatables:
            obj.update(dt)
        
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