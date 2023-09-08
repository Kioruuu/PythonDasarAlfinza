import tkinter as tk

def calculate_total():
    # Mengambil nilai dari inputan harga dan jumlah
    harga = float(entry_harga.get())
    jumlah = int(entry_jumlah.get())

    # Menghitung total harga
    total = harga * jumlah

    # Menampilkan total harga pada label
    label_total.config(text=f"Total Harga: Rp {total:.2f}")

# Membuat window utama
root = tk.Tk()
root.title("Program Kasir")

# Membuat label dan entry untuk harga
label_harga = tk.Label(root, text="Harga:")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

# Membuat label dan entry untuk jumlah
label_jumlah = tk.Label(root, text="Jumlah:")
label_jumlah.pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol untuk menghitung total
button_hitung = tk.Button(root, text="Hitung Total", command=calculate_total)
button_hitung.pack()

# Label untuk menampilkan total harga
label_total = tk.Label(root, text="Total Harga: Rp 0.00")
label_total.pack()

# Menjalankan aplikasi
root.mainloop()
