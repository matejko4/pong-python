import pygame as pg

from entities.entity import Entity  # Nadtřída Entity
from settings import PLAYER_SPEED, WIDTH, HEIGHT 

# Třída hráče
class Player(Entity):
    # Inicializace hráče
    def __init__(self, game, pos, keys, color=(250, 0, 0)):
        super().__init__(game, pos, size=(15, 100), color=color)  # Vytvoř hráče (15x100 pixelů)
        self.speed = PLAYER_SPEED 
        self.keys = keys  # Uloží si které klávesy ovládají tohoto hráče

    # Aktualizace hráče každý snímek
    def update(self, dt):
        keys = pg.key.get_pressed()
        # Vypočíta rychlost: y směr = dolů (1) - nahoru (-1)
        vel = pg.Vector2(0, keys[self.keys[1]] - keys[self.keys[0]])
        
        # Normalizuj (aby se hráč nepohyboval rychleji diagonálně)
        if vel.length() > 0:
            vel = vel.normalize()
        
        # Aktualizuje pozici
        self.pos += vel * dt * self.speed
        # Zabezpeči aby hráč nevyjel mimo obrazovku
        self.pos.y = max(50, min(self.pos.y, HEIGHT - 50))
        self.rect.center = self.pos