from random import choice, randint, shuffle
from constants import UC_LETTERS, LC_LETTERS, DIGITS, SYMBOLS

class PasswordGenerator():
    def __init__(self):
        self.password = ""
        self.password_list = []
        self.uc_letter_count = 0
        self.lc_letter_count = 0
        self.digit_count = 0
        self.symbol_count = 0

    # this is assuming that we are randomly choosing the number of characters to go into each password.
    # we can also give the user this option if we'd like to make it a little more customizable.
    def generate_password(self):
        self.uc_letter_count = randint(2,4)
        self.lc_letter_count = randint(8,10)
        self.digit_count = randint(2,4)
        self.symbol_count = randint(2,4)
        password_uc_letters = [choice(UC_LETTERS) for _ in range(self.uc_letter_count)]
        password_lc_letters = [choice(LC_LETTERS) for _ in range(self.lc_letter_count)]
        password_digits = [choice(DIGITS) for _ in range(self.digit_count)]
        password_symbols = [choice(SYMBOLS) for _ in range(self.symbol_count)]
        self.password_list = password_uc_letters + password_lc_letters + password_digits + password_symbols
        shuffle(self.password_list)
        self.password = "".join(self.password_list)

        return self.password