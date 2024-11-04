#menghentikan perulangan while
hitungan = 0

while True:  # Perulangan tak terbatas
    hitungan += 1
    print("Hitungan:", hitungan)
    
    if hitungan >= 5:  # Hentikan perulangan ketika hitungan mencapai 5
        break

print("Perulangan dihentikan.")

#menghentikan perulangan for
buah = ['apel', 'jeruk', 'mangga', 'pisang', 'anggur']

for item in buah:
    if item == 'pisang':  # Hentikan perulangan ketika menemukan 'pisang'
        break
    print("Buah:", item)

print("Perulangan dihentikan.")

#menggunakan break dengan input pengguna
while True:
    angka = int(input("Masukkan angka positif (0 untuk keluar): "))
    
    if angka == 0:  # Hentikan perulangan jika angka yang dimasukkan adalah 0
        break
    
    print("Anda memasukkan:", angka)

print("Program selesai.")