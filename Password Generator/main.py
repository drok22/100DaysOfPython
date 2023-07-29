from tkinter import *
from password_generator_view import PasswordGeneratorView


# ------------------MAIN-------------------#
def main():
    pw_generator_view = PasswordGeneratorView()
    # Runloop
    pw_generator_view.window.mainloop()

# --------------------------#
if __name__ == "__main__":
    main()