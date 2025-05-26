import pygame
from tetris.tetris import Tetris

def main():
    pygame.init()
    game = Tetris()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
