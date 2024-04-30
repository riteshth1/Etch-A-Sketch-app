from turtle import Turtle,Screen
from random import randint


screen = Screen()
is_race_on = False
screen.bgcolor("black")

# setup the screen of the turtle

screen.setup(width=600,height=600)

user_choice = screen.textinput(title="Make you bet", prompt="Choose the turtle color? You think win: ").lower()
colors = ["red", "orange", "purple", "yellow", "violet", "Blue"]

turtle_list = []

#Creating a list of coordinate to maintain proper spacing among the turtles

y_position = [-70, -40, -10, 20, 50, 80]

# creating multiple turtle object and setting their position all to the beginning

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x = -290,y = y_position[i])
    turtle_list.append(timmy)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 280: # The stopping point of turtles 300-(40/2) = 280 i.e the turtle is of 40x40
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won. The {winning_color} is the winner.")
            else:
                print(f"You've lose. The {winning_color} is the winner.")
        random_distance = randint(0, 10)
        turtle.fd(random_distance)

screen.exitonclick()