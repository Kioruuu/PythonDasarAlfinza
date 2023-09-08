import math

# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * (jari_jari ** 2) * tinggi
    return volume

# Fungsi untuk menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Input dari pengguna
pilihan = input("Pilih bentuk (tabung / balok): ")

if pilihan == "tabung":
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi_tabung = float(input("Masukkan tinggi tabung: "))
    volume_tabung = hitung_volume_tabung(jari_jari, tinggi_tabung)
    print(f"Volume tabung adalah: {volume_tabung:.2f} satuan kubik")
elif pilihan == "balok":
    panjang_balok = float(input("Masukkan panjang balok: "))
    lebar_balok = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))
    volume_balok = hitung_volume_balok(panjang_balok, lebar_balok, tinggi_balok)
    print(f"Volume balok adalah: {volume_balok:.2f} satuan kubik")
else:
    print("Pilihan tidak valid")
