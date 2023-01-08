class Cell:
    def __init__(self,x,y,flag):
        self.x = x
        self.y = y
        self.is_alive = flag

    def check_neighbours(self):
        num = 0 # how many neighbours this cell has
        for i in range(3):
            for j in range(3):
                if (i==1 and j==1) or (self.y - 1 + i)<0 or (self.y - 1 + i)>=len(grid) or (self.x - 1 + j)<0 or (self.x - 1 + j)>=len(grid[0]): continue
                if grid[self.y - 1 + i][self.x - 1 + j]==1: 
                    num+=1

        return num

    def change_state(self):
        n = self.check_neighbours()

        if self.is_alive:
            if n != 2 and n != 3:
                self.is_alive = 0
                # TODO: we dont need this method cause grid redraws every iteration
                rect = pygame.Rect(self.x*size, self.y*size, size, size)
                pygame.draw.rect(scene, (0,0,0), rect, 1) #TODO how to clear this rect
        else:
            if n == 3:
                self.is_alive = 1
                #TODO: change gamescene and draw a new cell
                rect = pygame.Rect(self.x*size, self.y*size, size, size)
                pygame.draw.rect(scene, (75, 139, 59), rect, 1)



import pygame, sys
import pygame.key
black = (0, 0, 0)
white = (21, 21, 21)
h, w = 800, 800
size = 20 #the size of the grid block
rows = h//size #how many rows
columns = w//size #how many columns
grid = [[0]*columns for j in range(rows)] #TODO: write properly

def main():
    global scene, clock, grid
    pygame.init()
    scene = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    scene.fill(black)
    is_auto = 0

    drawGrid()
    pygame.display.update()

    while True:
    #TODO make button start again
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid = new_generation()
                    pygame.display.update()
                if event.key == pygame.K_0:
                    is_auto = (is_auto+1)%2

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                grid[y//size][x//size]=1
                rect = pygame.Rect(x//size * size, y//size * size, size, size)
                pygame.draw.rect(scene, (75, 139, 59), rect, 1)
                pygame.display.update()
        if is_auto:
            #TODO change frame rate
            grid = new_generation()
            pygame.display.update()

def drawGrid():
    for x in range(0, w, size):
        for y in range(0, h, size):
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(scene, white, rect, 1)

def new_generation():
    new_grid = []
    for el in grid:
        new_grid.append(el[::])
    for y in range(40):
        for x in range(40):
            cell = Cell(x,y,grid[y][x])
            cell.change_state()
            new_grid[y][x] = cell.is_alive
    return new_grid
main()