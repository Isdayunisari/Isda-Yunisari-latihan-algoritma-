#operato Aritmatika
a = 2
b = 1
c = 10
d = 2
print(a+b)
print(a-b)
print(c*d)
print(c/d)

#operator perbandingan 
a = 2
b = 3
print(a<b)
print(b>a)

#operator logika
#and 
a = 2
b = 3

if a > 0 and b > 0:
    print("Keduanya positif")
else:
    print("Salah satu atau keduanya tidak positif")
#or
a = -4
b = 6

if a > 0 or b > 0:
    print("Salah satu dari a atau b positif")
else:
    print("Keduanya tidak positif")
#not
is_raining = False

if not is_raining:
    print("Cuaca cerah, silakan keluar!")
else:
    print("Bawa payung!")
    
#operator penugasan
#penjumlahan
a = 2
a += 3 
print(a)  
#pengurangan
x = 10
x -= 4  
print(x)  
#perkalian
c = 2
c *= 4  
print(c)  
#pembagian
e = 10
e /= 2 
print(e)  
#modulo
h = 5
h %= 3  
print(h)  

#operator bitwise
#and
a = 10  
b = 3  
result = a & b
print(result)
#or
a = 12  
b = 5   
result = a | b  
print(result)    
#not
a = 12  
result = ~a  
print(result)  

#operator keanggotaan
#menggunakan in dangan list
fruits = ['apple', 'banana', 'cherry']

if 'banana' in fruits:
    print("Banana ada dalam daftar buah.")
else:
    print("Banana tidak ada dalam daftar buah.")
#menggunakan not in dengan list
fruits = ['apple', 'banana', 'cherry']

if 'orange' not in fruits:
    print("Orange tidak ada dalam daftar buah.")
else:
    print("Orange ada dalam daftar buah.")
#menggunakan in dengan string
text = "Hello, world!"

if 'world' in text:
    print("Kata 'world' ada dalam string.")
else:
    print("Kata 'world' tidak ada dalam string.")
#menggunakan not in dengan tuple
numbers = (1, 2, 3, 4, 5)

if 6 not in numbers:
    print("Angka 6 tidak ada dalam tuple.")
else:
    print("Angka 6 ada dalam tuple.")
 #menggunakan in dengan dictionarya
 person = {'name': 'Alice', 'age': 30}

if 'name' in person:
    print("Kunci 'name' ada dalam dictionary.")
else:
    print("Kunci 'name' tidak ada dalam dictionary.")
#menggunakan not in dengan set
unique_numbers = {1, 2, 3, 4, 5}

if 6 not in unique_numbers:
    print("Angka 6 tidak ada dalam set.")
else:
    print("Angka 6 ada dalam set.")
    

#operator identitas
#menggunakan is untuk membandingkan objek
a = [1, 2, 3]
b = a  

if a is b:
    print("a dan b adalah objek yang sama.")
else:
    print("a dan b adalah objek yang berbeda.")
 #menggunkan is dengan tipe data yang berbeda
 a = [1, 2, 3]
b = [1, 2, 3]  # b adalah list baru dengan nilai yang sama

if a is b:
    print("a dan b adalah objek yang sama.")
else:
    print("a dan b adalah objek yang berbeda.")