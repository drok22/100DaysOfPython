from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    #---------------------------------------------------------------------------------------------------------------
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        true_image = PhotoImage(file="Quizzler/images/true.png")
        false_image = PhotoImage(file="Quizzler/images/false.png")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_clicked)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_clicked)

        # Default question text.
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, width=300, font=("Arial", 20, "italic"))

        self.setup_grid()
        self.get_next_question()

        self.window.mainloop()
    
    #---------------------------------------------------------------------------------------------------------------
    def setup_grid(self):
        # Row 0
        self.score_label.grid(row=0, column=1)
        # Row 1
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Row 2
        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=0)
    
    #---------------------------------------------------------------------------------------------------------------
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")

        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

            self.canvas.itemconfig(self.question_text, text=f"You've finished the quiz! Final score: {self.quiz_brain.score} points!")

    #---------------------------------------------------------------------------------------------------------------
    def true_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    #---------------------------------------------------------------------------------------------------------------
    def false_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    #---------------------------------------------------------------------------------------------------------------
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
