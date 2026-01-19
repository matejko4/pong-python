import pygame as pg
from entities.entity import Entity  # Nadtřída
from settings import BALL_SPEED, WIDTH, HEIGHT  

class Ball(Entity):
    def __init__(self, game, pos, direction):
        super().__init__(game, pos, size=(10, 10), color=(0, 255, 0))
        self.direction = direction  # Směr pohybu míče

    # Aktualizace míče
    def update(self, dt):
        # Pohyb míče
        self.pos += self.direction * BALL_SPEED * dt
        self.rect.center = self.pos
        
        # Kontrola kolize se stěnou
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction.y *= -1  # Obrati Y směr
        
        # Kontrola zda míč vyletěl mimo obrazovku
        if self.rect.left <= 0:  # Vpravo
            self.game.score_p2 += 1  # Player2 získá bod
            self.kill()  # Smaže míč
        elif self.rect.right >= WIDTH:  # Vlevo
            self.game.score_p1 += 1  # Player1 získá bod
            self.kill()  
        
        # Kontrola kolize s hráči
        if pg.sprite.spritecollide(self, [self.game.player1, self.game.player2], False):
            self.direction.x *= -1  # Obrati X směr (doprava -> doleva)