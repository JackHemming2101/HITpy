class Resistor:
    def __init__(self,x,y,resist):
        self.position_x = x
        self.position_y = y
        self.resist = resist

    def show_position(self):
        return([self.position_x,self.position_y,])

class Link:
    def __init__(self,x,y,x2,y2):
        self.position_start_x = x
        self.position_start_y = y
        self.position_end_x = x2
        self.position_end_y = y2

    def show_position(self):
        print(self.position_start_x,self.position_start_y,self.position_end_x,self.position_end_y)
