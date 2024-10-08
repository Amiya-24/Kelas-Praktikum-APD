import os

def clean():
    os.system("cls")

clean() # dipakai untuk membersihkan tampilan terminal

# #                                                          DEKLARASI DICTIONARY
# #          CONTOH 1
# daftar_buah = {
#     "buah1" : "apel",
#     "buah2" : "jeruk",
#     "buah3" : "mangga",
#     "buah4" : "pisang"
# }

# print(daftar_buah["buah1"])
# print(daftar_buah["buah2"])
# print(daftar_buah["buah3"])
# print(daftar_buah["buah4"])

# #          CONTOH 2
# daftar_buah = {}
# daftar_buah["buah1"] = "apel"
# daftar_buah["buah2"] = "jeruk"
# daftar_buah["buah3"] = "mangga"
# daftar_buah["buah4"] = "pisang"

# print(daftar_buah)


# #                                                          SIFAT DICTIONARY
# #          UNIQUE
# #(jika terdapat lebih dari satu value dengan 'key' yang sama, maka value dengan 'key' yang terakhir didefinisikanlah yang diambil)
# komik = {
#     "judul" : "one piece",
#     "judul" : "naruto",
#     "judul" : "dragon ball",
#     "judul" : "horimiya"
# }

# print(komik["judul"])

# #                                                          MEMBUAT DICTIONARY
# #          SINGLE ITEM
# nama_dict = {
#     "key" : "value"
# }

# #          MULTIPLE ITEM
# nama_dict = {
#     "key1" : "value",
#     "key2" : "value",
#     "key3" : "value"
# }

# #          CONTOH 1
# bio = {
#     "Nama" : "Muhammad Faiz Lazuardi",
#     "Nim" : 2409106031,
#     "Kelas" : "A24",
#     "KRS" : ["APD","LI","Kalkulus"],
#     "Mahasiswa_Aktif" : True,
#     "Sosmed" : {
#         "instagram" : "@lazuardi.2408",
#         "discord" : "Amiya#4674"
#     }
# }

# #          MENGGUNAKAN dict()
# bio = dict(nama = "faiz", nim = "031", kelas = "A24")
# print(bio)

# #                                                          MENGAKSES ITEM
# #          MENGGUNAKAN []
# print(f"""
# Nama        : {bio['Nama']}
# Nim         : {bio['Nim']}
# Kelas       : {bio['Kelas']}
# Instagram   : {bio['Sosmed']['instagram']}
# Discord     : {bio['Sosmed']['discord']}
# """)

# #           MENGGUNAKAN .get()
# print(f"""
# Nama        : {bio.get('Nama')}
# Nim         : {bio.get('Nim')}
# Kelas       : {bio.get('Kelas')}
# KRS         : {bio.get('KRS')[2]}
# Instagram   : {bio.get('Sosmed')['instagram']}
# Discord     : {bio.get('Sosmed')['discord']}
# """)

# #                                                          PERULANGAN
# bio = {
#     "Nama" : "Muhammad Faiz Lazuardi",
#     "Nim" : 2409106031,
#     "Kelas" : "A",
#     "Angkatan" : 24
# }

# #           TIDAK MENGGUNAKAN .items
# for i in bio:
#     print(i)
# print(" ")

# #           MENGGUNAKAN .items
# for i,j in bio.items():
#     print(f"{i} : {j}")
# print("")

# #       CARA LAIN
# for i in bio:
#     print(f"{i} : {bio[i]}")

# #                                                          MENAMBAHKAN ITEM
# hero = {
#     "nata" : "asassin",
#     "gatot" : "tank",
#     "miya" : "mm",
#     "xavier" : "mage",
# }
# print(hero)

# #           MENGGUNAKAN []
# hero["aamon"] = "asassin"
# print(hero)

# #           MENGGUNAKAN .update
# hero.update({"valentina" : "mage"})
# print(hero)

# #                                                          MENGUBAH ITEM
# hero = {
#     "nata" : "asassin",
#     "gatot" : "tank",
#     "miya" : "mm",
#     "xavier" : "mage",
# }
# print(hero)

# #           MENGGUNAKAN []
# hero["miya"] = "marksman"
# print(hero)

# #           MENGGUNAKAN .update
# hero.update({"xavier" : "mid"})
# print(hero)

# #                                                          MENGHAPUS ITEM
# hero = {
#     "nata" : "asassin",
#     "gatot" : "tank",
#     "miya" : "mm",
#     "xavier" : "mage",
# }
# print(hero)

# #          MENGGUNAKAN del()
# del hero["miya"]
# print(hero)
# print(hero.get("miya"))

# #          MENGGUNAKAN pop()
# trash_bin = hero.pop("gatot")
# print(hero)
# print(hero.get("gatot"))
# print(trash_bin)    # yang dipanggil 'value'nya bukan 'key'nya

# #          MENGGUNAKAN clear()
# hero.clear() # menghapus semua isi dictionary
# print(hero)

# #                                                           BEBERAPA FUNGSI YANG BISA DIPAKAI
# bio = {
#     "Nama" : "Muhammad Faiz Lazuardi",
#     "Nim" : 2409106031,
#     "Kelas" : "A",
#     "Angkatan" : 24
# }

# #          MENGETAHUI PANJANG DICTIONARY MENGGUNAKAN len()
# print("jumlah data = ", len(bio))

# #          MEMBUAT SALINAN DARI DICTIONARY MENGGUNAKAN copy()
# simpan = bio.copy()
# print("Biodata:", simpan)

# #          MEMBUAT DICTIONARY MENGGUNAKAN DATA YANG TELAH KITA SIAPAKAN MENGGUNAKAN fromkeys()
# key = "apel","jeruk","mangga","pisang"
# value = 1
# buah = dict.fromkeys(key,value)
# print(buah)

# #           KEYS AND VALUE
# for i in bio.keys():
#     print(i)

# print("")

# for j in bio.values():
#     print(j)

# #                                                         SET DEFAULT
# bio = {
#     "Nama" : "Muhammad Faiz Lazuardi",
#     "Nim" : 2409106031,
#     "Kelas" : "A",
#     "Angkatan" : 24
# }

# print(bio)
# print("Hobi : ", bio.setdefault("Hobi","Membaca"))
# bio.setdefault("Kesukaan","Tidur")
# print(bio)

# #                                                         DICTIONARY OF LIST AND NESTED DICTIONARY
# mahluk_hidup = {
#     "hewan darat" : ["ayam","kucing","beruang"],
#     "ikan" : ["lele","nila","hiu"],
#     "burung" : ["elang","garuda"]
# }

# for i, j in mahluk_hidup.items():
#     print(f"{i} adalah: ")
#     for hewan in j:
#         print(hewan)
#     print("")

# mahasiswa = {
#     31 : {"Nama" : "Faiz","Kelas" : "A"},
#     10 : {"Nama" : "Zeydan","Kelas" : "A"},
#     29 : {"Nama" : "Ridho","Kelas" : "A"},
#     46 : {"Nama" : "Nabil", "Kelas" : "A"}
# }
# for i, j in mahasiswa.items():
#     print("NIM Mahasiswa :",i)
#     for i_a, j_a in j.items():
#         print(i_a, ":", j_a)
#     print("")

# #           MENAMBAHKAN ITEM
# mahasiswa[31]["Gender"] = "Laki-Laki"
# print(mahasiswa)

# #           MENGUBAH ITEM
# mahasiswa[46]["Kelas"] = "B"
# print(mahasiswa)

# #           CONTOH HASIL
# for i, j in mahasiswa.items():
#     print("NIM Mahasiswa :",i)
#     for i_a, j_a in j.items():
#         print(i_a, ":", j_a)
#     print("")

# #           MENGHAPUS ITEM
# del mahasiswa[46]["Kelas"]
# print(mahasiswa)
# del mahasiswa[46]
# print(mahasiswa)

# print("Hello, World")

# #                                                             STUDI KASUS 1
# bio = {
#     "Nama" : "Muhammad Faiz Lazuardi",
#     "Nim" : 2409106031,
#     "Umur" : 18,
#     "Angkatan" : 24,
#     "Jurusan" : "Informatika"
# }
# print("Biodata Awal")
# for i,j in bio.items():
#     print(f"{i} : {j}")
# print("")

# print("Biodata Setelah Menambahkan Items")
# bio.update({"Fakultas" : "Teknik"})
# for i,j in bio.items():
#     print(f"{i} : {j}")
# print("")

# print("Biodata Setelah Mengubah Items")
# bio.update({"Umur" : 20})
# for i,j in bio.items():
#     print(f"{i} : {j}")
# print("")

# print("Biodata Setelah Menghapus Items")
# del bio["Fakultas"]
# for i,j in bio.items():
#     print(f"{i} : {j}")
# print("")


# #                                                              STUDI KASUS 2
# mapel = {
#     'Matematika' : 90,
#     'Fisika' : 80,
#     'Biologi': 80,
#     'Kimia' : 70
# }

# for i,j in mapel.items():
#     print(f"{i} : {j}")
# print("")

# total = sum(mapel.values())
# print("Nilai total : ", total)
# rata = total / len(mapel)
# print("Nilai rata-rata : ", rata)