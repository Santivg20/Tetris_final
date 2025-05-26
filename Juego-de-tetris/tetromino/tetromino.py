import random
from settings.settings import ancho_tablero
from shapes.shapes import formas
from colors.colors import colores

class Tetromino:
    def __init__(self):
        self.forma_idx = random.randint(0, len(formas) - 1)
        self.forma = [row[:] for row in formas[self.forma_idx]]
        self.color = colores[self.forma_idx]
        self.x = ancho_tablero // 2 - len(self.forma[0]) // 2
        self.y = 0

    def rotate(self):
        self.forma = [[self.forma[y][x] for y in range(len(self.forma) - 1, -1, -1)]
                      for x in range(len(self.forma[0]))]
