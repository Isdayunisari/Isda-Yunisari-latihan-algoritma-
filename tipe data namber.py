#tipe data number ada tiga yaitu float,integer,dan bilangan kompleks
#tipe data integer
x = 1000
y = -500
z = 0

# Operasi aritmatika dengan integer
penjumlahan = x + y #1000+(-500)
print(penjumlahan)  

# Perkalian
perkalian = 4 * 3 
print(perkalian)  

# Pembagian bulat
angka = 10 /2
print(angka)  

# Menggunakan integer dalam loop
for i in range(5):
    print(i)  

# tipe data float
a = 10.5
b = -3.14
c = 1.23e4  # Eksponensial (sama dengan 12300.0)

# Operasi aritmatika dengan float
hasil = a + b  # 10.5 + (-3.14)
print(hasil)  
# Penggunaan float dalam fungsi matematika
import math
sqrt_value = math.sqrt(a)  # Akar kuadrat dari a
print(sqrt_value)  

#tipe data bilangan kompleks
a1 = 9 + 15j
b2 = 8 - 12j

# Menampilkan bagian real dan imajiner
print("Bagian real a1:", a1.real)  
print("Bagian imajiner a1:", a1.imag) 

# Operasi aritmatika pada bilangan kompleks
penjumlahan = a1 + b2 
print("Hasil penjumlahan:", penjumlahan)

perkalian = a1 * b2  
print("Hasil perkalian:", perkalian)

# Fungsi bilangan kompleks
konjugasi = a1.conjugate() 
print("Konjugat a1:", konjugasi)


