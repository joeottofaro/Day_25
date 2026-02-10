# Class was built mostly to clean up the main.py code
from turtle import Turtle


class WriteToMap(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def state_name(self, x, y, state):
        """ Will write a state name at the given coordinates """
        self.goto(x, y)
        self.write(state, align="center", font=("Arial", 6, "bold"))
