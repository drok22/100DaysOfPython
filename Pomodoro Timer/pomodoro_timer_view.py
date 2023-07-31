import math
from tkinter import *
from constants import *

class PomodoroTimerView():
    def __init__(self):
        self.reps = 0
        self.timer = None

        self.window = Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        tomato_image = PhotoImage(file="Pomodoro Timer/tomato.png")

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=tomato_image)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

        self.check_marks = Label(text="", fg=GREEN, bg=YELLOW)
        self.title_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
        self.start_button = Button(text="Start", highlightthickness=0, command=self.start_timer)
        self.reset_button = Button(text="Reset", highlightthickness=0, command=self.reset_timer)
        self.check_marks = Label(text="", fg=GREEN, bg=YELLOW)
        #self.reset_timer()

        # Row 0
        self.title_label.grid(column=1, row=0)
        # Row 1
        self.canvas.grid(column=1, row=1)
        # Row 2
        self.start_button.grid(column=0, row=2)
        self.reset_button.grid(column=2, row=2)
        # Row 3
        self.check_marks.grid(column=1, row=3)

        # if you put this in main() then the tomato doesn't show up... but why?
        self.window.mainloop()
    
    #---------------------------------------------------------------------
    def start_timer(self):
        self.reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg=PINK)
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    #---------------------------------------------------------------------
    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="")
        self.check_marks.config(text="")
        self.reps = 0

    #---------------------------------------------------------------------
    def count_down(self, count):

        count_min = math.floor(count / 60)
        count_sec = count % 60

        if count_min == 0:
            count_min = ""

        if(count_sec < 10):
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marks = ""
            work_sessions = math.floor(self.reps/2)
            for _ in range(work_sessions):
                marks += "✔"
            self.check_marks.config(text=marks)