from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_PATH = "Snake/high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(HIGH_SCORE_PATH) as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.display_logo()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def display_logo(self):
        self.color("aquamarine4")
        self.goto(0, 100)
        self.write(".▄▄ ·  ▐ ▄  ▄▄▄· ▄ •▄ ▄▄▄ .", align = ALIGNMENT, font = FONT)
        self.goto(0, 80)
        self.write("▐█ ▀. •█▌▐█▐█ ▀█ █▌▄▌▪▀▄.▀·", align = ALIGNMENT, font = FONT)
        self.goto(0, 60)
        self.write("▄▀▀▀█▄▐█▐▐▌▄█▀▀█ ▐▀▀▄·▐▀▀▪▄", align = ALIGNMENT, font = FONT)
        self.goto(0, 40)
        self.write("▐█▄▪▐███▐█▌▐█ ▪▐▌▐█.█▌▐█▄▄▌", align = ALIGNMENT, font = FONT)
        self.goto(0, 20)
        self.write(" ▀▀▀▀ ▀▀ █▪ ▀  ▀ ·▀  ▀ ▀▀▀ ", align = ALIGNMENT, font = FONT)
        self.color("white")
        self.goto(0,0)
        self.write("PRESS SPACE TO PLAY", align = ALIGNMENT, font = FONT)
        self.goto(0,-20)
        self.write("PRESS ESC TO QUIT", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def start_game(self):
        self.goto(0, 270)
        self.update_scoreboard()        

    def game_over(self):
        if self.score > self.high_score:
            self.goto(0, 80)
            self.write("NEW HIGH SCORE!!!", align = ALIGNMENT, font = FONT)
            
        self.goto(0,20)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        self.goto(0,-20)
        self.write("PRESS SPACE TO PLAY AGAIN", align = ALIGNMENT, font = FONT)
        self.goto(0,-40)
        self.write("PRESS ESC TO QUIT", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake/high_score.txt", "w") as data:
                data.write(f"{self.high_score}")
                
        self.score = 0
        self.update_scoreboard()

