from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# Etch-A-Sketch App
def move_forward():
    """Function to move your turtle pen forward"""
    timmy.fd(10)


def move_backward():
    """Function to move your turtle pen backward"""
    timmy.left(180)


def counter_clockwise():
    """Function to move your turtle pen counter clockwise"""
    timmy.left(10)

def clock_wise():
    """Function to move your turtle pen clockwise"""
    timmy.right(10)


def clear_screen():
    """Function to clear the screen"""
    screen.resetscreen()

def not_line():
    """Pen up"""
    timmy.penup()

def pen_down():
    """pen down"""
    timmy.pendown()

# helps to listen your keystroke
screen.listen()

# function as an input
screen.onkey(key="w", fun=move_forward)
screen.onkey(move_backward,"s")
screen.onkey(counter_clockwise,"a")
screen.onkey(clock_wise,"d")
screen.onkey(clear_screen,"c")
screen.onkey(not_line,"p")
screen.onkey(pen_down,"o")


# holds the screen
screen.exitonclick()