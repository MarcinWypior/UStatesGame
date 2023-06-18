import turtle
import pandas

ALIGNMENT = "center"

FONT = ("Arial", 16, "normal")
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
data_frame = pandas.read_csv("50_states.csv")
list_of_states = data_frame.state.tolist()

screen.addshape(image)
turtle.shape(image)

guessed_states = []
def write_state_name(state_name, x, y):
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto((int(x), int(y)))
    pen.write(f"{state_name}", align=ALIGNMENT, font=FONT)


while len(guessed_states) < 40:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name ?").title()
    print(answer_state)

    if answer_state =="Exit".title():
        break;
    if answer_state in list_of_states:
        # print("is in list")
        # print(data_frame[data_frame["state" == answer_state]])
        state_data = data_frame[data_frame["state"] == answer_state]
        write_state_name(answer_state, state_data.x, state_data.y)
        guessed_states.append(answer_state)

    screen.update()


if not answer_state =="Exit".title():
    FONT = ("Arial", 100, "normal")
    write_state_name("You Won !!!", 0,0)
    print("You Won")
else:
    states_to_learn = list(set(list_of_states).difference(guessed_states))
    states_to_learn.sort()

    for state in states_to_learn:
        print(state)

