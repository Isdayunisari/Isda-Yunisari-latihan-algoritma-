#Percabangan Kondisi If Else If Bahasa Python
umur = int(input("Masukkan umur Anda: "))

if umur < 13:
    print("Anda masih anak-anak.")
elif umur < 20:
    print("Anda remaja.")
elif umur < 60:
    print("Anda dewasa.")
else:
    print("Anda sudah lanjut usia.")
