import pygame
import random

class Cell():
    def __init__(self,pos):
        self.position = pos
        self.state = 0 # 0 is empty 1 is has some food 2 is accupyied
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


class Feild():
    def __init__(self,screen):
        self.screen = screen
        self.board =
        self.cells = []
        self.cell_size = 80
        self.init()

    def init(self):
        self.init_cells()

    def init_cells(self):
        for x in range(0,8):
            for y in range(0,8):
                x_pos = x * self.cell_size
                y_pos = y * self.cell_size
                pos = (x_pos,y_pos)
                cell = Cell(pos)
                self.cells.append(cell)

class Game():
    def __init__(self):
pygame.init()

# this is the main scrren
screen = pygame.display.set_mode((1000,1000))
screen.fill((255,255,255))

# this would be the area that game flows
board = pygame.draw.rect(screen,(0,0,0),(100,100,800,800))


feild = Feild()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()