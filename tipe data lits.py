# Membuat list dengan berbagai tipe data
 nama = [10, 20, 30, "isda", True]

# Mengakses elemen dalam list
print("Elemen pertama:", nama[0])  
print("Elemen terakhir:", nama[-1])  

# Mengubah elemen pada indeks tertentu
nama[1] = 50
print("List setelah mengubah elemen:", nama) 
# Menambahkan elemen baru ke akhir list,menggunakan (append) untuk menambahkan elemen baru
nama.append("Baru")
print("List setelah penambahan elemen:", nama)  
# Menghapus elemen berdasarkan nilai,menggunakan (.remove) untuk menghapus elemen di list
nama.remove(30)
print("List setelah penghapusan elemen:", nama) 

# Mengakses elemen dengan indeks negatif
print("Elemen terakhir:", nama[-1])  

# Mengurutkan list angka
angka = [3, 1, 4, 2, 5]
#menggunakan (sort)untuk mengurutkan list angka
angka.sort()
print("List setelah diurutkan:", angka) 
# Membalik urutan elemen dalam list
angka.reverse()
print("List setelah dibalik:", angka)  

# Menggabungkan dua list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_gabungan = list_1 + list_2
print("List gabungan:", list_gabungan)  # Output: [1, 2, 3, 4, 5, 6]
