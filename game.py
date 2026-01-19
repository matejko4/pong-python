# Importy - knihovny a třídy které potřebuji
import pygame as pg  
from entities.player import Player  
from entities.ball import Ball  
from settings import WIDTH, HEIGHT, FPS 

# Hlavní třída hry - řídí celou aplikaci
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # Vytvoří okno hry s daným rozměrem
        pg.display.set_caption('Pong')  # Nastaví název okna
        self.clock = pg.time.Clock()  # Hodiny na měření FPS (rychlosti hry)
        self.font = pg.font.Font(None, 36)  # Font pro text (skóre a zprávy)

        # Skupina všech objektů, která se budou zobrazovat
        self.all_sprites = pg.sprite.Group()

        # Vytvoříme dva hráče - player1 vlevo (W,S), player2 vpravo (šipky)
        self.player1 = Player(game=self, pos=(50, HEIGHT / 2), keys=(pg.K_w, pg.K_s), color=(250, 0, 0))  # červený
        self.player2 = Player(game=self, pos=(WIDTH - 50, HEIGHT / 2), keys=(pg.K_UP, pg.K_DOWN), color=(0, 0, 255))  # modrý
        self.all_sprites.add(self.player1)  # Přidáme je do skupiny spritů
        self.all_sprites.add(self.player2)

        self.balls = pg.sprite.Group()  # Skupina míčů
        self.running = True  # Proměnná která kontroluje zda hra běží
        self.score_p1 = 0  # Skóre hráče 1
        self.score_p2 = 0  # Skóre hráče 2
        self.winner = None  # Vítěz (None = nikdo, 1 = player1, 2 = player2)

    # Hlavní herní smyčka - běží pořád dokud je running = True
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000  
            self.handle_events()  
            self.update(dt)  
            self.draw() 

    # Zpracování vstupních událostí (klávesy, zavření okna...)
    def handle_events(self):
        for event in pg.event.get():  # Projde všechny události
            if event.type == pg.QUIT:  
                self.running = False  # Ukončí hru
            elif event.type == pg.KEYDOWN:  # Pokud je stisknuta klávesa
                if event.key == pg.K_SPACE and not self.balls:  # Pokud SPACE a míč není v hře
                    if self.winner:  # Pokud je vítěz, resetuj skóre a vítěze
                        self.score_p1 = self.score_p2 = 0
                        self.winner = None
                    # Vytvoří míč a dá mu směr
                    ball = Ball(self, (WIDTH / 2, HEIGHT / 2), pg.Vector2(1, 0.5).normalize())
                    self.balls.add(ball)
                    self.all_sprites.add(ball)

    # Aktualizace logiky hry
    def update(self, dt):
        if not self.winner:  # Pouze pokud hra běží (není vítěz)
            self.all_sprites.update(dt)  # Aktualizuj všechny objekty (hráče, míč)
            # Zkontroluj podmínky vítězství
            if self.score_p1 >= 10:
                self.winner = 1
            elif self.score_p2 >= 10:
                self.winner = 2

    # Vykreslovani 
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)  # Nakresli všechny objekty
        
        # Nakresli skóre v horní části
        self.screen.blit(self.font.render(f'{self.score_p1} : {self.score_p2}', True, (255, 255, 255)), (WIDTH / 2 - 30, 20))
        
        # Pokud je vítěz ukáže zprávu a instrukce
        if self.winner:
            self.screen.blit(self.font.render(f'Player {self.winner} wins!', True, (255, 255, 0)), (WIDTH / 2 - 100, HEIGHT / 2 - 50))
            self.screen.blit(self.font.render('Press SPACE to play again', True, (255, 255, 255)), (WIDTH / 2 - 170, HEIGHT / 2 + 20))
        elif not self.balls:  
            self.screen.blit(self.font.render('Press SPACE to start', True, (255, 255, 255)), (WIDTH / 2 - 150, HEIGHT / 2)) 
        
        pg.display.flip()  # Aktualizuje obrazovku