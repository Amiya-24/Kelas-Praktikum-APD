import os

def clean():
    os.system("cls")

clean() # dipakai untuk membersihkan tampilan terminal


#                   ValueError
angka = int(input("Masukkan angka: ")) #input “Hello”
print(angka)


#                   Try-Except
try: # dicoba dulu di try, jika terjadi error maka akan langsung masuk ke except
    angka = int(input("Masukkan angka: "))

except ValueError: # except ... (bisa error apa saja, tidak pasti ValueError)
    print("Input yang anda masukkan bukan angka")


#                 Try-Except-Else
try: # dicoba dulu di try, jika terjadi error maka akan langsung masuk ke except
    angka = int(input("Masukkan angka: "))

except ValueError: # except ... (bisa error apa saja, tidak pasti ValueError)
    print("Input yang anda masukkan bukan angka")

else: # akan dijalankan jika tidak terjadi error pada try
    print(f"Angka yang kamu input: {angka}")


#             Try-Except-Else-Finally
try: # dicoba dulu di try, jika terjadi error maka akan langsung masuk ke except
    angka = int(input("Masukkan angka: "))

except ValueError: # except ... (bisa error apa saja, tidak pasti ValueError)
    print("Input yang anda masukkan bukan angka")

else: # akan dijalankan jika tidak terjadi error pada try
    print(f"Angka yang kamu input: {angka}")

finally: # akan selalu dijalankan walau program mengalami error
    print("Program selesai")


#                   kustom Error
try:
    nama = input("Hello, what's your name? ")
    if len(nama) > 5:
        raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# dengan menggunakan 'raise' kita dapat menyesuaikan output apa yang akan keluar jika terdapat error

except ValueError as e: # tidak mesti menggunakan 'e'
    print(e)




#                   External File
