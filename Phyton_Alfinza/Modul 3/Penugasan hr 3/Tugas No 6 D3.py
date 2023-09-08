import turtle
import math

# Define some colors
blue = (0, 0, 1)
red = (1, 0, 0)
white = (1, 1, 1)
dark_blue = (0, 0, 0.4)
light_gray = (0.8, 0.8, 0.8)

# Define some constants
PI = math.pi
RADIUS = 100  # The radius of the logo circle
SMK_FONT_SIZE = 16
PRESTASI_FONT_SIZE = 14

# Create a turtle object
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)

# Move the turtle to a position
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw a circle with a given radius and color
def circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw a text with a given font, size, and color
def text(text, font, size, color):
    t.fillcolor(color)
    t.write(text, font=(font, size, "normal"))

# Draw the logo circle
move(0, -RADIUS)
circle(RADIUS, white)  # White background
move(0, -RADIUS)
t.pencolor(blue)
t.circle(RADIUS)  # Blue border

# Draw the "SMK" text
move(-30, -10)
text("SMK", "Arial", SMK_FONT_SIZE, dark_blue)

# Draw the "PRESTASI PRIMA" text
move(-70, -60)
text("PRESTASI", "Arial", PRESTASI_FONT_SIZE, red)
move(-70, -80)
text("PRIMA", "Arial", PRESTASI_FONT_SIZE, red)

# Draw additional details (triangles)
t.pencolor(light_gray)
t.fillcolor(light_gray)
t.begin_fill()

for _ in range(2):
    t.forward(60)
    t.right(120)
    t.forward(60)
    t.left(120)

t.end_fill()

# Close the turtle graphics window on click
turtle.exitonclick()

# Keep the window open
turtle.mainloop()
