import PySimpleGUI as sg
from datetime import datetime

# Dictionary untuk menyimpan data kendaraan (nomor polisi, waktu masuk)
data_kendaraan = {}
histori_nomor_polisi = []

# Tema PySimpleGUI
sg.theme('LightGrey1')

# Layout untuk input data kendaraan saat masuk
layout_input_masuk = [
    [sg.Text("Nomor Polisi:"), sg.InputText(key="-POLISI-MASUK-")],
    [sg.Button("Masuk Kendaraan")]
]

# Layout untuk input data kendaraan saat keluar
layout_input_keluar = [
    [sg.Text("Nomor Polisi:"), sg.InputText(key="-POLISI-KELUAR-")],
    [sg.Text("Waktu Keluar (HH:MM):"), sg.InputText(key="-KELUAR-")],
    [sg.Button("Hitung Biaya Parkir")]
]

# Layout untuk menampilkan hasil biaya parkir
layout_hasil = [
    [sg.Text("", size=(30, 1), key="-HASIL-")],
]

# Layout utama
layout = [
    [sg.Frame("Input Data Kendaraan (Masuk)", layout_input_masuk)],
    [sg.Frame("Input Data Kendaraan (Keluar)", layout_input_keluar)],
    [sg.Frame("Hasil", layout_hasil)],
    [sg.Text("Cari Nomor Polisi:"), sg.InputText(key="-CARI-"), sg.Button("Cari Kendaraan")],
    [sg.Frame("Histori Nomor Polisi", [[sg.Listbox(values=histori_nomor_polisi, size=(30, 6), key="-HISTORI-")]])]
]

# Membuat window utama
window = sg.Window("Program Parkir", layout)

def hitung_biaya(waktu_masuk, waktu_keluar):
    try:
        waktu_masuk = datetime.strptime(waktu_masuk, "%H:%M")
        waktu_keluar = datetime.strptime(waktu_keluar, "%H:%M")

        selisih = waktu_keluar - waktu_masuk

        tarif_per_jam = 2000
        biaya_parkir = (selisih.total_seconds() / 3600) * tarif_per_jam

        return f"Biaya Parkir: Rp {biaya_parkir:.2f}"

    except ValueError:
        return "Format waktu salah"

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Masuk Kendaraan":
        nomor_polisi_masuk = values["-POLISI-MASUK-"]
        waktu_masuk = datetime.now().strftime("%H:%M")
        data_kendaraan[nomor_polisi_masuk] = (waktu_masuk, None, None)  # Simpan waktu masuk
        histori_nomor_polisi.append(nomor_polisi_masuk)
        window["-HISTORI-"].update(histori_nomor_polisi)
        sg.popup(f"Kendaraan dengan nomor polisi {nomor_polisi_masuk} masuk pada waktu {waktu_masuk}")

    if event == "Hitung Biaya Parkir":
        nomor_polisi_keluar = values["-POLISI-KELUAR-"]
        waktu_keluar = values["-KELUAR-"]

        if nomor_polisi_keluar in data_kendaraan:
            waktu_masuk, _, _ = data_kendaraan[nomor_polisi_keluar]
            hasil = hitung_biaya(waktu_masuk, waktu_keluar)
            data_kendaraan[nomor_polisi_keluar] = (waktu_masuk, waktu_keluar, hasil)
            window["-HASIL-"].update(hasil)
        else:
            window["-HASIL-"].update("Nomor polisi tidak ditemukan")

    if event == "Cari Kendaraan":
        nomor_polisi_cari = values["-CARI-"]
        if nomor_polisi_cari in data_kendaraan:
            waktu_masuk, waktu_keluar, biaya_parkir = data_kendaraan[nomor_polisi_cari]
            if waktu_keluar:
                window["-HASIL-"].update(f"Masuk: {waktu_masuk} - Keluar: {waktu_keluar}, {biaya_parkir}")
            else:
                window["-HASIL-"].update(f"Masuk: {waktu_masuk} - Belum Keluar")
        else:
            window["-HASIL-"].update("Nomor polisi tidak ditemukan")

window.close()
