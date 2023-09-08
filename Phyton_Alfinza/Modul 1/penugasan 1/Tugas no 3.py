# Input dari pengguna
awal = int(input("Masukkan nilai awal: "))
akhir = int(input("Masukkan nilai akhir: "))

# Mencetak nilai ganjil dan genap dalam rentang tertentu
print("Nilai ganjil dalam rentang {} sampai {}: ".format(awal, akhir))
for i in range(awal, akhir + 1):
    if i % 2 != 0:
        print(i, end=" ")

print("\nNilai genap dalam rentang {} sampai {}: ".format(awal, akhir))
for i in range(awal, akhir + 1):
    if i % 2 == 0:
        print(i, end=" ")
