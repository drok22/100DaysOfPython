from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
LEFT_SCORE_X = -100
RIGHT_SCORE_X = 100
SCORE_Y = 200

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE_X, SCORE_Y)
        self.write(self.left_score, align = ALIGNMENT, font = FONT)
        self.goto(RIGHT_SCORE_X, SCORE_Y)
        self.write(self.right_score, align = ALIGNMENT, font = FONT)

    def left_scored(self):
        self.right_score += 1
        self.update_scoreboard()

    def right_scored(self):
        self.left_score += 1
        self.update_scoreboard()
