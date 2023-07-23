import pandas
import turtle

STATES_TO_LEARN = "US States Game/missing_states.csv"
STATES_IMAGE = "US States Game/blank_states_img.gif"
STATES_DATA = "US States Game/50_states.csv"

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
# add background image as a shape, then set it
screen.addshape(STATES_IMAGE)
turtle.shape(STATES_IMAGE)

all_states_data = pandas.read_csv(STATES_DATA)
all_states = all_states_data.state.to_list()

def get_mouse_click(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click)

guessed_states = []

while len(guessed_states) < len(all_states):
    answer = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", 
                              prompt = "What's another state's name?").title()
    
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv(STATES_TO_LEARN)
        break

    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = all_states_data[all_states_data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer)

#turtle.mainloop()
#screen.exitonclick()