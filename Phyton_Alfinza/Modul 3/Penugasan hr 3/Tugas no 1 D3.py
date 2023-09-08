import turtle

def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(side_length, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

def draw_trapezium(base1, base2, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.forward(base1)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
    turtle.forward(base2)
    turtle.left(135)
    turtle.forward(height)
    turtle.end_fill()

def draw_parallelogram(base, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.forward(base)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward(base)
    turtle.left(45)
    turtle.forward(height)
    turtle.end_fill()

def draw_rhombus(side_length, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

def main():
    turtle.speed(1)  # Kecepatan gambar (1 lambat, 10 cepat)

    # Set up the window size to fit the drawings
    turtle.setup(width=800, height=400)

    # Move turtle to initial position for the first shape
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.pendown()

    # Gambar persegi panjang dengan warna biru
    draw_rectangle(100, 50, "blue")

    # Pindah ke posisi berikutnya
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    # Gambar segitiga dengan warna kuning
    draw_triangle(100, "yellow")

    # Pindah ke posisi berikutnya
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()

    # Gambar trapezium dengan warna hijau
    draw_trapezium(100, 150, 50, "green")

    # Pindah ke posisi berikutnya
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()

    # Gambar jajar genjang dengan warna merah
    draw_parallelogram(100, 50, "red")

    # Pindah ke posisi berikutnya
    turtle.penup()
    turtle.goto(250, 0)
    turtle.pendown()

    # Gambar belah ketupat dengan warna orange
    draw_rhombus(70, "orange")

    # Tutup layar saat selesai menggambar
    turtle.exitonclick()

if __name__ == "__main__":
    main()
