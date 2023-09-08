import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_arc(color, radius, x, y, start_angle, end_angle):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x + radius, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(start_angle)
    for _ in range(int((end_angle - start_angle) / 2)):
        turtle.forward(radius * 3.14 / 180)
        turtle.left(2)
    turtle.end_fill()

def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_person():
    # Kepala
    draw_circle("yellow", 40, 0, 0)

    # Mata kiri
    draw_circle("white", 8, -20, 20)
    draw_circle("black", 4, -20, 20)

    # Mata kanan
    draw_circle("white", 8, 20, 20)
    draw_circle("black", 4, 20, 20)

    # Hidung
    draw_circle("red", 5, 0, 10)

    # Mulut
    draw_arc("black", 20, 0, -10, -60, 60)

    # Badan
    draw_line(0, 0, 0, -80)

    # Tangan kiri
    draw_line(0, -60, -30, -30)

    # Tangan kanan
    draw_line(0, -60, 30, -30)

    # Kaki kiri
    draw_line(0, -80, -20, -120)

    # Kaki kanan
    draw_line(0, -80, 20, -120)

    # Tutup layar saat selesai menggambar
    turtle.done()

# Inisialisasi layar dan turtle
screen = turtle.Screen()
screen.setup(width=400, height=400)  # Atur ukuran layar

# Panggil fungsi untuk menggambar orang
draw_person()

# Tunggu hingga pengguna menutup jendela
turtle.exitonclick()
