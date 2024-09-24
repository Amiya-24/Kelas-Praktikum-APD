import os

def clean():
    os.system("cls")

clean() # dipakai untuk membersihkan tampilan terminal


#                                                           PENGULANGAN FOR
# ulang = 11 # dimulai dari 0 dan berakhir di 10
# print("Banyak Perulangan Yang Dilakukan Adalah:")
# for i in range(ulang):
#     print("Perulangan ke-" + str(i))

# mahasiswa = [2409106031, "Faiz", 0.31, True, "A2'24"]
# for i in mahasiswa:
#     print(i) #menampilkan output secara bertahap (kebawah)
# print(mahasiswa) #menampilkan output secara langsung (kekanan)

# for i in range(5, 11): # dimulai dari 5 dan berakhir di 10
#     for j in range(1, 11): # dimulai dari 1 dan berakhir di 10
#         print(f"{i} x {j} = {i*j}")
#     print() #digunakan untuk memberi spasi antar perkalian diatas

#                                                          PENGULANGAN WHILE
# jawab = "Y"
# hitung = 0
# while (jawab == "Y"):
#     print(f"Pengulangan ke-{hitung}")
#     print("Yakin Ingin Mengulang (Y/N)")
#     hitung += 1
#     jawab = input("yakin ngulang? ")
#     clean()
# print(f"total pengulangan: {hitung}")

# hitung = 0
# while True:
#     print(f"Pengulangan ke-{hitung}")
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     clean()
#     if ulang == "tidak" or ulang == "Tidak" or ulang == "ga" or ulang == "Ga" or ulang == "g" or ulang == "G" or  ulang == "":
#         break
# print(f"Total Perulangan: {hitung}")

# print("Daftar bilangan genap dari 1-10")
# for i in range(1, 11): # dimulai dari 1 dan berakhir di 10
#     if i % 2 == 1: 
#         continue # kalau memenuhi syarat maka dia dilewati, jika beda maka dia akan di print
#     print(i)


#                                                             Studi Kasus 2
# total = 0
# angka = 0

# while angka >= 0:
#     angka = int(input("Masukkan Angka: "))
#     if angka < 0:
#         break
#     total += angka

# print("Jumlah total dari inputan adalah:", total)
