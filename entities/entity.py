import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, game, pos, size, color):
        super().__init__() 
        self.game = game  # Odkaz na hru 

        # Vytvoří obraz
        self.image = pg.Surface(size)
        self.image.fill(color)  

        # Pozice
        self.pos = pg.Vector2(pos)
        self.rect = self.image.get_rect(center=pos)  # Obdélník pro kolize

   
    def update(self, dt):
        pass  