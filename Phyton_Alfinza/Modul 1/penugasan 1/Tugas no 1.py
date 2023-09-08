def hitung_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi ** 2
    return keliling, luas

def hitung_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return keliling, luas

def hitung_trapesium(alas1, alas2, tinggi, sisi1, sisi2):
    keliling = alas1 + alas2 + sisi1 + sisi2
    luas = 0.5 * (alas1 + alas2) * tinggi
    return keliling, luas

pilihan = input("Pilih bentuk (persegi / persegi panjang / trapesium): ")

if pilihan == "persegi":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    keliling, luas = hitung_persegi(sisi)
elif pilihan == "persegi panjang":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    keliling, luas = hitung_persegi_panjang(panjang, lebar)
elif pilihan == "trapesium":
    alas1 = float(input("Masukkan panjang alas atas trapesium: "))
    alas2 = float(input("Masukkan panjang alas bawah trapesium: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    sisi1 = float(input("Masukkan panjang sisi sejajar 1 trapesium: "))
    sisi2 = float(input("Masukkan panjang sisi sejajar 2 trapesium: "))
    keliling, luas = hitung_trapesium(alas1, alas2, tinggi, sisi1, sisi2)
else:
    print("Pilihan tidak valid")

if pilihan:
    print(f"Keliling {pilihan} adalah: {keliling}")
    print(f"Luas {pilihan} adalah: {luas}")
