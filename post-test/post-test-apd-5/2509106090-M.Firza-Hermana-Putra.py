import os

# ======== DATA AWAL ========
user = [
    ["admin", "123", "admin"],
    ["firza", "090", "user"]
]

barang = [
    ["Keyboard Logitech", 500000],
    ["Item Wibu", 400000],
    ["Meja Gaming Tapan", 5000000],
    ["Mouse INNO X3", 410000],
    ["Headset Rexus", 300000],
    ["Kursi Gaming", 1500000]
]

# ======== FUNGSI UMUM ========
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nTekan Enter untuk lanjut...")

# ======== REGISTER ========
def register():
    clear()
    print("=== REGISTER AKUN BARU ===")
    nama = input("Masukkan username baru: ")
    sandi = input("Masukkan password baru: ")
    ada = False

    for u in user:
        if u[0] == nama:
            ada = True

    if ada:
        print("Username sudah digunakan!")
    else:
        user.append([nama, sandi, "user"])
        print("Akun berhasil dibuat!")
    pause()

# ======== LOGIN ========
def login():
    clear()
    print("=== LOGIN ===")
    nama = input("Masukkan username: ")
    sandi = input("Masukkan password: ")

    for u in user:
        if u[0] == nama and u[1] == sandi:
            print("Login berhasil!")
            pause()
            return u
    print("Username atau password salah!")
    pause()
    return None

# ======== MENU ADMIN ========
def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Lihat User")
        print("6. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            print("=== DAFTAR BARANG ===")
            for i in range(len(barang)):
                print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
            pause()

        elif pilih == "2":
            clear()
            nama = input("Nama barang: ")
            harga = input("Harga barang: ")
            if harga.isdigit():
                barang.append([nama, int(harga)])
                print("Barang berhasil ditambah!")
            else:
                print("Harga harus angka!")
            pause()

        elif pilih == "3":
            clear()
            for i in range(len(barang)):
                print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
            ubah = input("Pilih nomor barang: ")
            if ubah.isdigit():
                ubah = int(ubah)
                if 1 <= ubah <= len(barang):
                    nama_baru = input("Nama baru: ")
                    harga_baru = input("Harga baru: ")
                    if harga_baru.isdigit():
                        barang[ubah-1] = [nama_baru, int(harga_baru)]
                        print("Barang berhasil diubah!")
                    else:
                        print("Harga harus angka!")
                else:
                    print("Nomor tidak ditemukan!")
            else:
                print("Masukkan angka!")
            pause()

        elif pilih == "4":
            clear()
            for i in range(len(barang)):
                print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
            hapus = input("Pilih nomor barang: ")
            if hapus.isdigit():
                hapus = int(hapus)
                if 1 <= hapus <= len(barang):
                    barang.pop(hapus-1)
                    print("Barang berhasil dihapus!")
                else:
                    print("Nomor tidak ditemukan!")
            else:
                print("Masukkan angka!")
            pause()

        elif pilih == "5":
            clear()
            print("=== DAFTAR USER ===")
            for i in range(len(user)):
                print(f"{i+1}. {user[i][0]} - {user[i][2]}")
            pause()

        elif pilih == "6":
            break
        else:
            print("Pilihan tidak ada!")
            pause()

# ======== MENU USER ========
def menu_user(nama):
    keranjang = []

    while True:
        clear()
        print(f"=== MENU USER ({nama}) ===")
        print("1. Lihat Barang")
        print("2. Beli Barang")
        print("3. Lihat Keranjang & Bayar")
        print("4. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            print("=== DAFTAR BARANG ===")
            for i in range(len(barang)):
                print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
            pause()

        elif pilih == "2":
            clear()
            for i in range(len(barang)):
                print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
            beli = input("Pilih nomor barang (0 untuk batal): ")
            if beli.isdigit():
                beli = int(beli)
                if beli == 0:
                    pass
                elif 1 <= beli <= len(barang):
                    keranjang.append(barang[beli-1])
                    print(f"{barang[beli-1][0]} ditambahkan ke keranjang!")
                else:
                    print("Barang tidak ditemukan!")
            else:
                print("Masukkan angka!")
            pause()

        elif pilih == "3":
            clear()
            if len(keranjang) == 0:
                print("Keranjang kosong!")
            else:
                total = 0
                for i in range(len(keranjang)):
                    print(f"{i+1}. {keranjang[i][0]} - Rp{keranjang[i][1]}")
                    total += keranjang[i][1]
                print("-------------------")
                print(f"Total: Rp{total}")
                bayar = input("Bayar sekarang? (y/n): ")
                if bayar.lower() == "y":
                    print("Pembayaran berhasil! Terima kasih telah berbelanja 🙏")
                    keranjang.clear()
                else:
                    print("Pembayaran dibatalkan.")
            pause()

        elif pilih == "4":
            break
        else:
            print("Pilihan tidak tersedia!")
            pause()

# ======== PROGRAM UTAMA ========
while True:
    clear()
    print("=== TOKO PERALATAN GAMING ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        akun = login()
        if akun:
            if akun[2] == "admin":
                menu_admin()
            else:
                menu_user(akun[0])
    elif menu == "2":
        register()
    elif menu == "3":
        clear()
        print("Terima kasih telah berkunjung!")
        break
    else:
        print("Pilihan tidak ada!")
        pause()