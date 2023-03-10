import pygame
import random,time
class Cell():
    def __init__(self,row,column,size_width,size_height):
        self.size_width = size_width
        self.size_hieght = size_height
        self.row = row
        self.column = column
        self.x = self.column*self.size_width
        self.y = self.row*self.size_hieght
        self.state = 0 # 0 is empty 1 is has some food 2 is accupyied
        self.color = Colors.BACKGROUND_COLOR
class Snake():
    def __init__(self,currrnt_cell):
        self.head = None
        self.body = []
        self.tail = None

class Direction():
    STOP = (0,0)
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1)
    DOWN = (0,1)

class Colors():
    BACKGROUND_COLOR = (0,0,0)
    RED_COLOR = (255,0,0)
    GREEN_COLOR = (0,255,0)
    BLUE_COlOR = (0,0,255)

class Game():
    def __init__(self):
        pygame.init()
        self.gamestarted = 0 # 0 not started yet 1 is started
        self.height = 800
        self.width = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(Colors().BACKGROUND_COLOR)
        self.cell_size_width = 25
        self.cell_size_height = 25
        self.cell_count_x = self.width//self.cell_size_width
        self.cell_count_y = self.height//self.cell_size_height
        self.time_laps = 0.3
        self.player_curdire = Direction().STOP

        self.cells = []
        self.init_cells()
        self.player = []
        self.init_player()
        self.food = []
        self.food_generate()


    def run(self):
        running = True
        while running:
            time.sleep(self.time_laps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    self.gamestarted = 1
                    if event.key == pygame.K_LEFT and self.player_curdire != Direction.RIGHT:
                        self.player_curdire = Direction.LEFT
                    elif event.key == pygame.K_UP and self.player_curdire != Direction.DOWN:
                        self.player_curdire = Direction.UP
                    elif event.key == pygame.K_RIGHT and self.player_curdire != Direction.LEFT:
                        self.player_curdire = Direction.RIGHT
                    elif event.key == pygame.K_DOWN and self.player_curdire != Direction.UP:
                        self.player_curdire = Direction.DOWN


            if self.gamestarted:
                self.player_move()

            self.render_cells()
            pygame.display.update()
        pygame.quit()

    def init_cells(self):
        for cell_column in range(0,self.cell_count_x):
            for cell_row in range(0,self.cell_count_y):
                cell = Cell(cell_row,cell_column,self.cell_size_width,self.cell_size_height)
                self.cells.append(cell)

    def init_player(self):
        head = random.choice(self.cells)
        self.cell_convert_to_player(head)
        self.player.append(head)

    def food_generate(self):
        while True:
            food = random.choice(self.cells)
            if food.state == 0:
                self.cell_convert_to_food(food)
                self.food.append(food)
                return

    def cell_convert_to_blank(self,cell):
        cell.color = Colors().BACKGROUND_COLOR
        cell.state = 0
    def cell_convert_to_food(self,cell):
        cell.color = Colors().GREEN_COLOR
        cell.state = 1
    def cell_convert_to_player(self,cell):
        cell.color = Colors().BLUE_COlOR
        cell.state = 2
    def cell_conver_to_looserhead(self,cell):
        cell.color = Colors().RED_COLOR

    def player_move(self):
        tail = self.player[0]
        old_head = self.player[-1]
        new_head = self.get_cell_by_curdir()
        if new_head.state == 0:
            self.cell_convert_to_player(new_head)
            self.cell_convert_to_blank(tail)
            self.player.remove(tail)
            self.player.append(new_head)
        elif new_head.state == 1:
            self.cell_convert_to_player(new_head)
            self.player.append(new_head)
            self.food_generate()
        elif new_head.state == 2:
            self.gamestarted = 0
            print("You Loos")


    def get_cell_by_curdir(self):
        head = self.player[-1]
        cur_row = head.row
        cur_col = head.column
        cur_dir_x,cur_dir_y = self.player_curdire
        des_row = cur_row + cur_dir_y
        des_col = cur_col + cur_dir_x
        des_row = self.get_available_row(des_row)
        des_col = self.get_available_col(des_col)
        return self.get_cell_by_grid(des_row,des_col)

    def get_available_row(self,row):
        if row > -1:
            if not row < self.cell_count_y:
                row = 0
        else:
            row = self.cell_count_y - 1
        return row

    def get_available_col(self,column):
        if column > -1:
            if not column < self.cell_count_x:
                column = 0
        else:
            column = self.cell_count_x - 1
        return column

    def get_cell_by_grid(self,row,column):
        for cell in self.cells:
            if cell.row == row and cell.column == column:
                return cell
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