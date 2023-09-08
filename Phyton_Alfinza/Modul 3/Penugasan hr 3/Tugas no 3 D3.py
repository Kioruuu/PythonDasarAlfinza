import turtle

# Fungsi untuk menggambar segi empat dengan warna
def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Inisialisasi layar
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Atur ukuran layar sesuai dengan rasio Bendera Indonesia

# Pindah ke posisi awal merah di Bendera
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()

# Gambar bagian merah di atas Bendera
draw_rectangle(600, 100, "#FF0000")  # Warna merah dalam format heksadesimal

# Pindah ke posisi awal putih di Bendera
turtle.penup()
turtle.goto(-300, 100)
turtle.pendown()

# Gambar bagian putih di tengah Bendera
draw_rectangle(600, 100, "#FFFFFF")  # Warna putih dalam format heksadesimal

# Tutup layar saat selesai menggambar
turtle.done()

# Tunggu hingga pengguna menutup jendela
turtle.exitonclick()
