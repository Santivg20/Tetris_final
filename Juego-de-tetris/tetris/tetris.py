import pygame
from settings.settings import *
from colors.colors import *
from tetromino.tetromino import Tetromino
        
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[negro for _ in range(ancho_tablero)] for _ in range(altura_tablero)]
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.game_over = False
        self.score = 0
        self.fall_speed = 500  # milisegundos entre movimientos hacia abajo
        self.fall_time = 0
        self.font = pygame.font.Font(None, 36)
    
    def valid_move(self, piece, x, y):
        for i in range(len(piece.forma)):
            for j in range(len(piece.forma[i])):
                if piece.forma[i][j]:
                    if (x + j < 0 or x + j >= ancho_tablero or 
                            y + i >= altura_tablero or
                            (y + i >= 0 and self.grid[y + i][x + j] != negro)):
                        return False
        return True

    def lock_piece(self):
        for i in range(len(self.current_piece.forma)):
            for j in range(len(self.current_piece.forma[i])):
                if self.current_piece.forma[i][j]:
                    if self.current_piece.y + i <= 0:
                        self.game_over = True
                        return
                    self.grid[self.current_piece.y + i][self.current_piece.x + j] = self.current_piece.color

        if not self.game_over:
            self.clear_lines()
            self.current_piece = self.next_piece
            self.next_piece = Tetromino()

            # Verificar si la próxima pieza puede entrar en el tablero
            for i in range(len(self.current_piece.forma)):
                for j in range(len(self.current_piece.forma[i])):
                    if (self.current_piece.forma[i][j] and
                        self.grid[self.current_piece.y + i][self.current_piece.x + j] != negro):
                        self.game_over = True
                        return
    def clear_lines(self):
        lines_cleared = 0
        for i in range(len(self.grid)):
            if all(cell != negro for cell in self.grid[i]):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [negro for _ in range(ancho_tablero)])
        if lines_cleared:
            self.score += (100 * lines_cleared)

    def draw_grid(self):
        for i in range(altura_tablero):
            for j in range(ancho_tablero):
                pygame.draw.rect(self.screen, self.grid[i][j],(j * tamaño_bloque, i * tamaño_bloque, tamaño_bloque, tamaño_bloque))
                pygame.draw.rect(self.screen, gris,(j * tamaño_bloque, i * tamaño_bloque, tamaño_bloque, tamaño_bloque), width= 1)

        for i in range(len(self.current_piece.forma)):
            for j in range(len(self.current_piece.forma[i])):
                if self.current_piece.forma[i][j]:
                    pygame.draw.rect(self.screen, self.current_piece.color,
                                     ((self.current_piece.x + j) * tamaño_bloque,
                                        (self.current_piece.y + i) * tamaño_bloque,
                                           tamaño_bloque, tamaño_bloque))
        
        next_piece_text = self.font.render('Siguiente:', True, blanco) 
        self.screen.blit(next_piece_text, (ancho_tablero * tamaño_bloque + 20, 20)) 
        for i in range(len(self.next_piece.forma)):
            for j in range(len(self.next_piece.forma[i])):
                if self.next_piece.forma[i][j]:
                    pygame.draw.rect(self.screen, self.next_piece.color,
                                     (ancho_tablero * tamaño_bloque + 20 + j * tamaño_bloque,
                                           80 + i * tamaño_bloque,
                                           tamaño_bloque, tamaño_bloque))
        score_text = self.font.render(f'Puntaje: {self.score}', True, blanco)
        self.screen.blit(score_text, (ancho_tablero * tamaño_bloque + 20, 200))

    def run(self):
        while not self.game_over:
            self.fall_time += self.clock.get_rawtime()
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_move(self.current_piece, self.current_piece.x - 1, self.current_piece.y):
                            self.current_piece.x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_move(self.current_piece, self.current_piece.x + 1, self.current_piece.y):
                            self.current_piece.x += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                            self.current_piece.y += 1
                    elif event.key == pygame.K_UP:
                        original_shape = [row[:] for row in self.current_piece.forma]
                        self.current_piece.rotate()
                        if not self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y):
                            self.current_piece.forma = original_shape
            if self.fall_time >= self.fall_speed:
                if self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                    self.current_piece.y += 1
                else:
                    self.lock_piece()
                self.fall_time = 0

            self.screen.fill(negro)
            self.draw_grid()
            pygame.display.flip()

        game_over = True

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False

            # Oscurecer fondo
            dark_surface = pygame.Surface((ancho_pantalla, altura_pantalla))
            dark_surface.fill(negro)
            dark_surface.set_alpha(128)
            self.screen.blit(dark_surface, (0,0))

            # Mostrar mensaje de Game Over
            game_over_text = self.font.render('Game Over', True, blanco)
            score_text = self.font.render(f'Puntaje final: {self.score}', True, blanco)
            continue_text = self.font.render('Presiona X para salir', True, blanco)

            # Posicionar textos
            text_y = altura_pantalla // 2 - 60
            for text in [game_over_text, score_text, continue_text]:
                text_x = ancho_pantalla // 2 - text.get_width() // 2
                self.screen.blit(text, (text_x, text_y))
                text_y += 40

            pygame.display.flip()
