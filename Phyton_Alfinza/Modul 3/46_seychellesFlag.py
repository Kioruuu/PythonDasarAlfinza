import turtle

from PIL import Image


def save_as_jpg(canvas, fileName):
    canvas.postscript(file=fileName + ".eps")
    img = Image.open(fileName + ".eps")
    img.save(fileName + ".jpg", "jpeg")

def drawRectangle(ttl, x, y, width, height):
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.up()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.penup()

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

turtle.setup(1500, 1000, 0, 0)

myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myGreen = "#007336"
myWhite = "#FFFFFF"

Joe = turtle.Turtle()
Joe.screen.colormode(255)

drawRectangle(Joe, 0, 300, 600, 300)
Joe.goto(0, 0)

# Draw blue triangle
fillTriangle(Joe, 0, 0, 0, 300, 200, 300, myBlue)

# Draw yellow triangle
fillTriangle(Joe, 0, 0, 200, 300, 400, 300, myYellow)

# Draw red triangle
fillTriangle(Joe, 0, 0, 400, 300, 600, 300, myRed)

# Draw white triangle
fillTriangle(Joe, 0, 0, 600, 300, 600, 150, myWhite)

# Draw green triangle
fillTriangle(Joe, 0, 0, 600, 150, 600, 0, myGreen)

Joe.hideturtle()
ts = turtle.getscreen()
tc = ts.getcanvas()

# Save as JPEG
save_as_jpg(tc, "SeychellesFlag")
turtle.done()