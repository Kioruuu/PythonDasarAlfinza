umur = int(input("Masukkan umur: "))

if umur < 10:
  kategori = "Anak-anak"
elif umur < 18:
  kategori = "Remaja"
elif umur < 35:
  kategori = "Dewasa"
else:
  kategori = "Tua"

print("Kategori:", kategori)
