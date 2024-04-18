import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("yellow")

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)
t.width(3)  # Set the thickness of the lines

# Function to draw a star
def draw_star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

# Function to draw a spiral
def draw_spiral():
    length = 1
    angle = 91
    for _ in range(100):
        t.forward(length)
        t.right(angle)
        length += 2

# Set the initial position of the turtle for the star
t.penup()
t.goto(-50, 200)
t.pendown()

# Set the size of the star
size = 200

# Set the color of the lines
colors = ["blue", "red"]

# Draw the big star
for color in colors:
    t.color(color)
    draw_star(size)

# Set the initial position of the turtle for the spiral
t.penup()
t.goto(-150, -150)
t.pendown()

# Set the color of the spiral
t.color("blue")

# Draw the spiral
draw_spiral()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
