class renderer:
    def __init__(self,focal_length:int,color:tuple,window) -> None:
        self.fl = focal_length
        self.col = color
        self.window = window
        self.vertex_table = []
        self.line_table = []
    def _drawline(self,id):
        v1 = self.vertex_table[self.line_table[id][0]]
        v2 = self.vertex_table[self.line_table[id][1]]
        v1x = (self.fl*v1[0]/self.fl+v1[2])
        v1y = (self.fl*v1[1]/self.fl+v1[2])
        v2x = (self.fl*v2[0]/self.fl+v2[2])
        v2y = (self.fl*v2[1]/self.fl+v2[2])
        self.window.drawLine((round(v1x),round(v1y)),(round(v2x),round(v2y)))
    def draw(self):
        for i in range(len(self.line_table)):
            self._drawline(i)

if __name__ == "__main__":
    import redScreen
    screen = redScreen.screen(40)
    render = renderer(100,(127,127,127),screen)
    render.vertex_table = [
        (-5,5,1),
        (5,5,1),
        (5,-5,1),
        (-5,-5,1),
        (-5,5,11),
        (5,5,11),
        (5,-5,11),
        (-5,-5,11),
    ]
    render.line_table = [
        (0,1),
        (1,2),
        (2,3),
        (3,0),
        (4,5),
        (5,6),
        (6,7),
        (7,4),
        (0,4),
        (1,5),
        (2,6),
        (3,7)
    ]
    render.draw()
    screen.run()