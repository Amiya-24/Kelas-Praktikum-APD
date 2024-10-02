import os

def clean():
    os.system("cls")

clean() # dipakai untuk membersihkan tampilan terminal

# nama_ikan = ["lele","nila","koi"]
# print(nama_ikan)

# nama_ikan = [
#     "lele",
#     "nila",
#      "koi"
#      ]
# print(nama_ikan)

# tas = ["buku", 32, True, 3.14, ["IF", 24]]
# print(tas)

# MENAMBAHKAN DATA KEDALAM LIST
# .append digunakan untuk menambahkan data kedalam list
# biodata = ["Faiz", 18, 24.8]
# print(biodata)
# biodata.append("2006")
# print(biodata)
# biodata.append("samarinda")
# print(biodata)
# biodata.insert(1,"lazuardi")
# print(biodata)

# MENGGUBAH DATA YANG SUDAH ADA DI DALAM LIST
# [] setelah variabel digunakan untuk menggubah data yang sudah ada di dalam list
# biodata = ["Faiz", 18, 24.8]
# biodata[2] = "24"
# print(biodata)

# MENGHAPUS DATA YANG ADA DI DALAM LIST
# Menggunakan fungsi "del" untuk menghapus data yang sudah ada di dalam list
# biodata = ["Faiz", 18, 24.8]
# del biodata[2]
# print(biodata)
# del biodata[0]
# print(biodata)

# MEMISAHKAN DATA YANG ADA DIDALAM LIST
# menggunakan fungsi ".pop" untuk memisahkan data 
# pisah = biodata.pop(2)
# print(biodata)
# print(pisah)

# MEMILIH DIMANA AWAL DAN AKHIR
# "buah[0:4]"
# 0 digunakan sebagai awal dari list, tidak harus 0
# 4 digunakan sebagai akhir dari list
# jika ingin menampilkan jika ingin menampilkan 6 data maka isi dengan 6
# buah = ["apel","jeruk","anggur","pir","melon","semangka","kelengkeng"]
# print(buah[0:6])

# MELANGKAHI DATA YANG ADA DIDALAM LIST
# "var[0:7:3]""
# 0 digunakan sebagai awal dari list
# 7 digunakan sebagai akhir dari list
# 3 digunakan sebagai jumlah data yang dilangkahi
# buah = ["apel","jeruk","anggur","pir","melon","semangka","kelengkeng"]
# print(buah[0:3])
# print(buah[0:7:3])


# NESTED LIST
# Yaitu list didalam list
# biodata = ["faiz",18,["samarinda","kalimantan",["aws","air hitam",["apel","jeruk"]]]]
# print(biodata[1])
# print(biodata[2][1])
# print(biodata[2][2][1])
# print(biodata[2][2][2][1])

# OPERASI LIST
# warna_gelap = ["hitam","abu","biru tua"]
# warna_terang = ["putih","pink","biru muda"]
# semua = (warna_gelap + warna_terang)
# print(warna_gelap*3)
# print(semua)

# buah = [["apel","jeruk","anggur"],["pir","melon","semangka"],["kelengkeng","mangga"]]
# print(buah,"\n")
# print(buah[0],"\n")
# print(buah[1],"\n")
# print(buah[2],"\n")
# print(buah[2][1])


# barang = [["beruang", "koala", "kangguru"],"\n",
# ["kotak pensil", "penghapus", "pensil"]]
# #menampilkan semua barang
# for i in barang :
#     for k in i :
#         print (k)


#                                                              TUPLE
# tuple = ("faiz", 18, True, "baca")
# print(tuple[1])  
# print(tuple[3])
# print("\n")
# for u in (tuple):
#     print(u)


print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")