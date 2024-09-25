import os

def clean():
    os.system("cls")

clean() # dipakai untuk membersihkan tampilan terminal


# # #                                  PENGULANGAN FOR (kita menentukan berapa kali kita ingin mengulang)
# ulang = 11 # dimulai dari 0 dan berakhir di 10
# print("Banyak Perulangan Yang Dilakukan Adalah:")
# for i in range(ulang):
#     print("Perulangan ke-" + str(i))

# mahasiswa = [2409106031, "Faiz", 0.31, True, "A2'24"]
# for i in mahasiswa:
#     print(i) #menampilkan output secara bertahap (kebawah)
# print(mahasiswa) #menampilkan output secara langsung (kekanan)

# print("<=====Selamat datang di rumah minum IDS=====>")
# print("<===========Menu rumah minum IDS============>")

# menu = ["coca-cola","fanta","soda gembira","teh tarik","es kopi",]
# for i, minum in enumerate(menu,start=1):
#     print(f"{i}. {minum}")

# for i in range(len(menu)):
#     print(f"{i+1}. {menu[i]}")

# for i in range(5, 11): # dimulai dari 5 dan berakhir di 10
#     for j in range(1, 11): # dimulai dari 1 dan berakhir di 10
#         print(f"{i} x {j} = {i*j}")
#     print() #digunakan untuk memberi spasi antar perkalian diatas

# for i in range(5, 6): # dimulai dari 5 dan berakhir di 5 juga
#     for j in range(1, 6): # dimulai dari 1 dan berakhir di 5
#         for k in range(1, 6): # dimulai dari 1 dan berakhir di 5
#             print(f"{i} x {j} + {k} = {i*j+k}") 
#         print() #digunakan untuk memberi spasi antar perkalian diatas

# makan = ["bakso","mie ayam","lalapan lele"]
# minum = ["es teh","kopi","es jeruk"]

# for i in makan:
#     for j in minum:
#         print(f"{i} & {j}")
    # print()


# # #                                                        PENGULANGAN WHILE
# jawab = "Y"
# hitung = 0
# while (jawab == "Y" or jawab == "y"):
#     print(f"Pengulangan ke-{hitung}")
#     print("Yakin Ingin Mengulang (Y/N)")
#     hitung += 1
#     jawab = input("yakin ngulang? ")
#     clean()
# print(f"total pengulangan: {hitung}")

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# hitung = 0
# while True:
#     print(f"Pengulangan ke-{hitung}")
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     clean()
#     if ulang == "tidak" or ulang == "Tidak" or ulang == "ga" or ulang == "Ga" or ulang == "g" or ulang == "G" or  ulang == "":
#         print("oke kita break sejenak")
#         break
# print(f"Total Perulangan: {hitung}")

# # continue # kalau memenuhi syarat maka dia dilewati, jika beda maka dia akan di print
# print("Daftar bilangan genap dari 1-10")
# for i in range(1, 11): # dimulai dari 1 dan berakhir di 10
#     if i % 2 == 0: 
#         print(f"{i} Adalah Genap")
#         continue # dalam kondisi ini ga dipakai juga bisa
#     else:
#         print(f"{i} Adalah Ganjil")
#         continue # dalam kondisi ini ga dipakai juga bisa
#     print(i)

# # #                                                           Studi Kasus 2
total = 0
angka = 0

while angka >= 0:
    angka = int(input("Masukkan Angka: "))
    if angka < 0:
        break
    total += angka

print("Jumlah total dari inputan adalah:", total)