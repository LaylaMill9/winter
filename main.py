import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Wintery light blue background
screen.setup(width=800, height=800)  # Set the window size

# Create turtle for drawing
t = turtle.Turtle()
t.speed(10)


# Function to draw a rectangle (used for window, fireplace, etc.)
def draw_rectangle(color, width, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


# Function to draw a triangle (used for Christmas tree)
def draw_triangle(color, size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


# Function to draw a circle (used for decorations)
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)  # Adjust for center of the circle
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()


# Function to draw a Christmas tree
def draw_christmas_tree():
    # Tree base (green triangles)
    draw_triangle("green", 200, -100, -150)

    # Decorations on the tree (circles)
    draw_circle("red", 10, -50, -50)
    draw_circle("gold", 10, 10, -100)
    draw_circle("blue", 10, 40, -130)


# Function to draw a fireplace
def draw_fireplace():
    draw_rectangle("brown", 250, 100, -125, -250)
    draw_rectangle("black", 230, 80, -115, -240)

  # Tree trunk (brown rectangle)
    draw_rectangle("brown", 40, 60, -20, -210)


# Function to draw snow in the window
def draw_snowflakes():
    for x in range(-300, 300, 60):
        for y in range(100, 200, 60):
            draw_circle("white", 5, x, y)


# Function to draw a window
def draw_window():
    draw_rectangle("lightyellow", 250, 200, -125, 50)
    draw_rectangle("blue", 240, 190, -115, 60)  # Inside window (blue color)

    # Draw some snowflakes on the window (looking outside)
    draw_snowflakes()


# Draw the scene
draw_christmas_tree()
draw_fireplace()
draw_window()

# Hide the turtle after drawing
t.hideturtle()
