nama = input("Masukkan nama: ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

tunjangan = 0.2 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)

gaji_bersih = gaji_pokok + tunjangan - pajak

print("Nama:", nama)
print("Gaji Pokok:", gaji_pokok)
print("Gaji Bersih:", gaji_bersih)