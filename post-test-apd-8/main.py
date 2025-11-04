from login import login
from register import register

while True:
    print("Pilih Opsi:")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Masukan pilihan: ")

    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan harus 1-3")
