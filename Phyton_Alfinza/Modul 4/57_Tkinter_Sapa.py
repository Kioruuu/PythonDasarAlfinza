import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("sapa")

Nama_depan = tk.StringVar()
Nama_belakang = tk.StringVar()

def tombol_click():
    pesan = f"Hello {Nama_depan.get()}{Nama_belakang.get()}, Have a nice day"
    showinfo(title="hi", message=pesan)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

Nama_depan_label = ttk.Label(input_frame, text="Nama Depan : ")
Nama_depan_label.pack(padx=10, fill="x", expand=True)

Nama_depan_entry = ttk.Entry(input_frame, textvariable=Nama_depan)
Nama_depan_entry.pack(padx=10, fill="x", expand=True)

Nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang : ")
Nama_belakang_label.pack(padx=10, fill="x", expand=True)

Nama_belakang_entry = ttk.Entry(input_frame, textvariable=Nama_belakang)
Nama_belakang_entry.pack(padx=10, fill="x", expand=True)

tombol = ttk.Button(input_frame, text="Sapa", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()