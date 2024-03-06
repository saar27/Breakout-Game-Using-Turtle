from turtle import Turtle

FONT = ("courier",15,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lives = 4
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(150, 270)
        self.write(f"your score:{self.score}",move=False,align="center",font=FONT)
        self.goto(-150, 270)
        self.write(f"your lives:{self.lives}", move=False, align="center", font=FONT)

    def give_score(self):
        self.score += 1
        self.update_scoreboard()
    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()
    def win(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"YOU WIN", move=False, align="center", font=FONT)
    def lose(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"YOU lost", move=False, align="center", font=FONT)