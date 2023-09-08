tinggi = int(input("Masukkan jumlah baris segitiga: "))

for i in range(1, tinggi + 1):
    # Mencetak spasi sebelum bintang pertama pada setiap baris
    for j in range(tinggi - i):
        print(" ", end="")
    
    # Mencetak bintang pada setiap baris
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()
