#tipe data set digunakan untuk menyimpan sekumpulan elemen yang unik dan tidak terurut
set1 = {5, 6, 7, 8, 9}
set2 = {3, 4, 5, 6, 7}

#hasil tipe data set
print(set2)
print(set1)

#gabungan tipe data set(union)
print ("union:",set1.union(set2)) 

#irisan tipe data set(intersection)
print ("intrtsection:",set1.intersection(set2))

#selisih tipe data set(Difference)
print("Difference:",set1.difference(set2))

#menambahkan elemen baru ke tipe data set (add)
set1.add(6)
print("penambahan elemen baru:",set1)

#menghapus elemen yang ada di tipe data set(remove)
set2.remove(7)
print('menghapus elemen:',set2)