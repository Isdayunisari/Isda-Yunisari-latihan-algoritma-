#tipe data Dictionary/kamus python,yang berfungsi untuk menyimpan kumpulan data
print("python dictionary")
#1,menggunakan kurung kurawal
print('')#baris baru
data = {"nama" : "Baekhyun", "hobby" : "nyanyi", "tinggi" : "174", "umur" : "32"}
#cara mengakses pemanggilan
print("1.cara mencetak yang memunculkan hasilnya")
print(data)
print( "-nama:", Baekhyun["nama"])
print( "-hobby:", Baekhyun["hobby"])
print( "-tinggi:", Baekhyun["tinggi"])
print( "-umur:", Baekhyun["umur"])

print('')
#menggunakan dictionary/rungsi dictioanry
yadit = dict(
    nama = "Baekhyun", tinggi = "174", hobby = "nyanyi"
)
print("2.Cara Akses Item Pemanggilan")
print("Nama=", Baekhyun.get("nama"))
print("tinggi=", yadit.get("nim"))
print("hobby=", yadit.get("prodi"))

print('')
#metode kamus python menggunakan update
print("3.menggunakan update")
yadit.update ({"umur" : "33"})
print(data)