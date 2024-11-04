#menggunakan continue dalam perulangan for
angka = [1, 2, 3, 4, 5, 6]

for num in angka:
    if num % 2 == 0:  # Jika angka genap, lewati iterasi ini
        continue
    print("Angka ganjil:", num)
    