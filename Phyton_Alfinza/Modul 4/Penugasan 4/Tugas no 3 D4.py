import PySimpleGUI as sg

# Inisialisasi data siswa (dalam bentuk list)
data_siswa = []

# Tema PySimpleGUI
sg.theme('LightGrey1')

# Layout utama
layout = [
    [sg.Text("Program Data Siswa Baru", font=("Helvetica", 20))],
    [sg.Text("NISN:"), sg.InputText(key="-NISN-")],
    [sg.Text("Nama Siswa:"), sg.InputText(key="-NAMA-")],
    [sg.Text("Tanggal Lahir (dd/mm/yyyy):"), sg.InputText(key="-TANGGAL-")],
    [sg.Text("Asal Sekolah:"), sg.InputText(key="-SEKOLAH-")],
    [sg.Text("Nama Ayah:"), sg.InputText(key="-AYAH-")],
    [sg.Text("Nama Ibu:"), sg.InputText(key="-IBU-")],
    [sg.Text("Nomor Telepon:"), sg.InputText(key="-TELEPON-")],
    [sg.Text("Alamat:"), sg.InputText(key="-ALAMAT-")],
    [sg.Button("Tambah Data"), sg.Button("Tampilkan Data"), sg.Button("Simpan"), sg.Button("Reset")],
    [sg.Text("", size=(40, 1), key="-OUTPUT-")],
    [sg.Multiline("", size=(60, 10), key="-DATA-")],
    [sg.Button("Keluar")]
]

# Membuat window utama
window = sg.Window("Program Data Siswa Baru", layout)

def reset_form():
    window["-NISN-"].update("")
    window["-NAMA-"].update("")
    window["-TANGGAL-"].update("")
    window["-SEKOLAH-"].update("")
    window["-AYAH-"].update("")
    window["-IBU-"].update("")
    window["-TELEPON-"].update("")
    window["-ALAMAT-"].update("")
    window["-OUTPUT-"].update("")

def save_data(data):
    with open("data_siswa.txt", "w") as file:
        for siswa in data:
            file.write(f"{siswa[0]},{siswa[1]},{siswa[2]},{siswa[3]},{siswa[4]},{siswa[5]},{siswa[6]},{siswa[7]}\n")

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Keluar":
        break

    if event == "Tambah Data":
        nisn = values["-NISN-"]
        nama = values["-NAMA-"]
        tanggal_lahir = values["-TANGGAL-"]
        sekolah = values["-SEKOLAH-"]
        ayah = values["-AYAH-"]
        ibu = values["-IBU-"]
        telepon = values["-TELEPON-"]
        alamat = values["-ALAMAT-"]

        if nisn and nama and tanggal_lahir and sekolah and ayah and ibu and telepon and alamat:
            data_siswa.append((nisn, nama, tanggal_lahir, sekolah, ayah, ibu, telepon, alamat))
            window["-OUTPUT-"].update(f"Data siswa {nama} berhasil ditambahkan.")
            reset_form()
        else:
            window["-OUTPUT-"].update("Mohon lengkapi semua kolom.")

    if event == "Tampilkan Data":
        data_text = ""
        for siswa in data_siswa:
            data_text += f"NISN: {siswa[0]}, Nama: {siswa[1]}, Tanggal Lahir: {siswa[2]}, Asal Sekolah: {siswa[3]}, Ayah: {siswa[4]}, Ibu: {siswa[5]}, Telepon: {siswa[6]}, Alamat: {siswa[7]}\n\n"
        window["-DATA-"].update(data_text)

    if event == "Simpan":
        save_data(data_siswa)
        window["-OUTPUT-"].update("Data siswa berhasil disimpan ke 'data_siswa.txt'.")

    if event == "Reset":
        reset_form()

# Menutup window saat program selesai
window.close()