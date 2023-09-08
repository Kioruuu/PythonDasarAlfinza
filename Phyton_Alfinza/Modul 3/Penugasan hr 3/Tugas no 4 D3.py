import turtle

# Fungsi untuk menggambar pohon Fibonacci
def fibonacci_tree(turtle, branch_len, level):
    if level > 0:
        # Gambar batang pohon
        turtle.forward(branch_len)
        turtle.right(30)

        # Gambar cabang kanan (fibonacci_tree dengan tingkat level-1)
        fibonacci_tree(turtle, branch_len - 10, level - 1)

        # Putar kembali ke posisi sebelumnya
        turtle.left(60)

        # Gambar cabang kiri (fibonacci_tree dengan tingkat level-2)
        fibonacci_tree(turtle, branch_len - 10, level - 2)

        # Putar kembali ke posisi awal
        turtle.right(30)
        turtle.backward(branch_len)

# Inisialisasi layar dan turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Atur ukuran layar

fibonacci_turtle = turtle.Turtle()
fibonacci_turtle.speed(0)  # Kecepatan gambar maksimum

# Pindahkan turtle ke posisi awal
fibonacci_turtle.penup()
fibonacci_turtle.goto(0, -250)
fibonacci_turtle.setheading(90)
fibonacci_turtle.pendown()

# Panggil fungsi untuk menggambar pohon Fibonacci dengan tingkat rekursi 7
fibonacci_tree(fibonacci_turtle, 100, 7)

# Tutup layar saat selesai menggambar
turtle.done()

# Tunggu hingga pengguna menutup jendela
turtle.exitonclick()
