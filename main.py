# Draw class used to write state name on the map
import turtle
import pandas
from write_to_map import WriteToMap

# Screen setup
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


write_to_map = WriteToMap()
guessed_states = []

# Using pandas to read cvs and store states column as a list
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

# Loop will keep going til the user either types Exit or guesses all 50 states
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Used to append the states not in the guessed_states list to missing_states.
    # Panadas will create a DataFrame from missing_states list then store it as a csv
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Correct guesses get added to guessed_states list.
    # x/y cords are grabbed from the pandas data series as a row based off the state
    # .item() is used to grab the underlying data from the x|y column within that states row
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        write_to_map.state_name(state_data.x.item(), state_data.y.item(), answer_state)
