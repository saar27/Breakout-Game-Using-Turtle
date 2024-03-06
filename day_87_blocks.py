from turtle import Turtle

COLORS = ["blue","yellow","red",]

class BlockManger():
    def __init__(self):
        super().__init__()
        self.all_blocks = []
        self.create_blocks()

    def create_blocks(self):
        for row in range(3):
            for column in range(9):
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=2,stretch_len=2)
                new_block.color(COLORS[row])
                new_block.penup()
                new_block.goto(column*50-200,row*50+100)
                self.all_blocks.append(new_block)
    def remove_blocks(self,hitted_block):
        hitted_block.color("black")
        self.all_blocks.remove(hitted_block)