import pandas
import random
from tkinter import *
from constants import *

class FlashCardView():
    def __init__(self):
        self.deck = self.create_deck()
        self.current_card = {}
        
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

        #setup 3000ms timer
        self.flip_timer = None#self.window.after(3000, func=self.flip_card)

        self.canvas = Canvas(width=800, height=526)
        self.card_front_image = PhotoImage(file=CARD_FRONT)
        self.card_back_image = PhotoImage(file=CARD_BACK)
        self.card_display_image = self.canvas.create_image(400, 263, image=self.card_front_image)
        self.card_title = self.canvas.create_text(400, 150, text="Cliquez Pour Commencer", font=("Ariel", 40, "italic"), fill="black")
        self.card_word = self.canvas.create_text(400, 263, text="Click To Start", font=("Ariel", 60, "bold"), fill="black")

        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

        #Row 0
        self.canvas.grid(row=0, column=0, columnspan=2)
        #Row 1
        wrong_img = PhotoImage(file=WRONG_IMAGE)
        self.wrong_button = Button(command=self.wrong_clicked, image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR)
        self.wrong_button.grid(row=1, column=0)
        right_img = PhotoImage(file=RIGHT_IMAGE)
        self.right_button = Button(command=self.right_clicked, image=right_img, highlightthickness=0, background=BACKGROUND_COLOR)
        self.right_button.grid(row=1, column=1)

        # draw the first card
        # self.get_next_card()

        self.window.mainloop()

    #------------------------------------------
    def right_clicked(self):
        if(self.current_card in self.deck):
            self.deck.remove(self.current_card)

        # store for the next time that we 
        pandas.DataFrame(self.deck).to_csv(WORDS_TO_PRACTICE, index=False)

        self.get_next_card()

    #------------------------------------------
    def wrong_clicked(self):
        self.get_next_card()

    #------------------------------------------
    def get_next_card(self):
        # cancel existing timer
        if(self.flip_timer):
            self.window.after_cancel(self.flip_timer)

        # need to catch when we're at the end of the deck. will crash when the app 'finishes' running
        self.current_card = random.choice(self.deck)
        self.canvas.itemconfig(self.card_display_image, image=self.card_front_image)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")

        # give 3000ms before showing the correct answer again
        self.flip_timer = self.window.after(WAIT_TIMER_MS, func=self.flip_card)
    
    #------------------------------------------
    def flip_card(self):
        self.canvas.itemconfig(self.card_display_image, image=self.card_back_image)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")

    #------------------------------------------
    def create_deck(self):
        try:
            cards_to_practice = pandas.read_csv(WORDS_TO_PRACTICE).to_dict(orient="records")
        except:
            cards_to_practice = pandas.read_csv(FRENCH_WORDS).to_dict(orient="records")
            
        return cards_to_practice
