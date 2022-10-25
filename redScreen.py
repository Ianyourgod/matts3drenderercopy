import pygame
class screen:
    def __init__(self,size:int) -> None:
        self.size = size
        self.grid = []
        for i in range(size):
            self.grid.append([])
            for a in range(size):
                self.grid[i].append(False)
    def run(self):
        pygame.init()
        wind = pygame.display.set_mode((self.size*20,self.size*20))
        pygame.display.set_caption("Redstone Window")
        redoff = pygame.image.load("images/redstone_lamp.png").convert_alpha()
        redoff = pygame.transform.scale(redoff, (20, 20))
        redon = pygame.image.load("images/redstone_lamp_on.png").convert_alpha()
        redon = pygame.transform.scale(redon, (20, 20))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for y in range(len(self.grid)):
                for x in range(len(self.grid[y])):
                    if self.grid[y][x]:
                        wind.blit(redon,(x*20,y*20))
                    else:
                        wind.blit(redoff,(x*20,y*20))
            pygame.display.flip()
    def drawLine(self,start,end):
        x1,y1=start
        x2,y2=end
        x,y = x1,y1
        dx = abs(x2 - x1)
        dy = abs(y2 -y1)
        if dx==0:
            if y1 < y2:
                for i in range(y1,y2):
                    self.switchLamp(x1,i)
            else:
                for i in range(y2,y1):
                    self.switchLamp(x1,i)
            return
        try:
            if dy/float(dx) > 1:
                dx, dy = dy, dx
                x, y = y, x
                x1, y1 = y1, x1
                x2, y2 = y2, x2
        except:pass

        p = 2*dy - dx
        # Initialize the plotting points
        coords = [(x,y)]

        for k in range(2, dx + 2):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy

            x = x + 1 if x < x2 else x - 1
            coords.append((x,y))
        for i in coords:
            self.switchLamp(i[0],i[1])
    def switchLamp(self,x:int,y:int):
        self.grid[y+self.size//2-1][x+self.size//2-1] = not self.grid[y+self.size//2-1][x+self.size//2-1]