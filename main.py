import pygame
import random

class Cell():
    def __init__(self,pos):
        x,y = pos
        self.x = x
        self.y = y
        self.state = 0 # 0 is empty 1 is has some food 2 is accupyied
        self.color = Colors.BACKGROUND_COLOR
class Snake():
    def __init__(self,currrnt_cell):
        self.head = None
        self.body = []
        self.tail = None

class Colors():
    BACKGROUND_COLOR = (0,0,0)
    RED_COLOR = (255,0,0)
    GREEN_COLOR = (0,255,0)
    BLUE_COlOR = (0,0,255)

class Game():
    def __init__(self):
        pygame.init()
        self.height = 800
        self.width = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(Colors().BACKGROUND_COLOR)
        self.cell_size_width = 80
        self.cell_size_height = 80
        self.cell_count_x = self.width//self.cell_size_width
        self.cell_count_y = self.height//self.cell_size_height

        self.cells = []
        self.init_cells()
        self.init_player()

        self.player = []
        self.player_direction = (0,0)

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_LEFT]:
                self.player_direction = (-1,0)
            if key_input[pygame.K_UP]:
                self.player_direction = (0,-1)
            if key_input[pygame.K_RIGHT]:
                self.player_direction = (1,0)
            if key_input[pygame.K_DOWN]:
                self.player_direction = (0,1)
            self.render_cells()
            pygame.display.update()
        pygame.quit()

    def init_cells(self):
        for cell_column in range(0,self.cell_count_x):
            x_pos = cell_column * self.cell_size_width
            for cell_row in range(0,self.cell_count_y):
                y_pos = cell_row * self.cell_size_height
                pos = (x_pos,y_pos)
                cell = Cell(pos)
                cell.color = Colors.RED_COLOR
                self.cells.append(cell)

    def init_player(self):
        player = random.choice(self.cells)
        player.color = Colors().BLUE_COlOR


    def render_cells(self):
        screen = self.screen
        for cell in self.cells:
            color = cell.color
            pos_x = cell.x
            pos_y = cell.y
            size_x,size_y = (self.cell_size_width,self.cell_size_height)
            pygame.draw.rect(screen,color,(pos_x,pos_y,size_x,size_y))

    def update_cells(self):
        pass




game = Game()
game.run()