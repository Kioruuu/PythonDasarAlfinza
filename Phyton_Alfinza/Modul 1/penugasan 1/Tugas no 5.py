tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    # Mencetak bintang pada setiap baris
    for j in range(i):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()
