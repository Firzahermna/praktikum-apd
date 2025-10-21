import os

# Data awal user dan barang
user = [
    ["admin", "123", "admin"],
    ["firza", "090", "user"]
]

barang = [
    ["Keyboard Logitech", 500000],
    ["Item Wibu", 400000],
    ["Meja Gaming", 5000000],
    ["Mouse INNO X3", 410000],
    ["Headset Rexus", 300000],
    ["Kursi Gaming", 1500000]
]

keranjang = []

menu_utama = True
while menu_utama:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== TOKO PERALATAN GAMING ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    # LOGIN
    if menu == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        nama = input("Masukkan username: ")
        sandi = input("Masukkan password: ")

        akun = None
        for u in user:
            if u[0] == nama and u[1] == sandi:
                akun = u
        if akun == None:
            print("Username atau password salah!")
            input("Tekan Enter...")
        else:
            print("Login berhasil!")
            input("Tekan Enter...")

            if akun[2] == "admin":
                menu_admin = True
                while menu_admin:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== MENU ADMIN ===")
                    print("1. Lihat Barang")
                    print("2. Tambah Barang")
                    print("3. Ubah Barang")
                    print("4. Hapus Barang")
                    print("5. Lihat User")
                    print("6. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== DAFTAR BARANG ===")
                        for i in range(len(barang)):
                            print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
                        input("Tekan Enter...")

                    elif pilih == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== TAMBAH BARANG ===")
                        nama_brg = input("Nama barang: ")
                        harga_brg = input("Harga barang: ")
                        if harga_brg.isdigit():
                            barang.append([nama_brg, int(harga_brg)])
                            print("Barang berhasil ditambah!")
                        else:
                            print("Harga harus berupa angka!")
                        input("Tekan Enter...")

                    elif pilih == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== UBAH BARANG ===")
                        for i in range(len(barang)):
                            print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
                        ubah = input("Pilih nomor barang: ")
                        if ubah.isdigit():
                            ubah = int(ubah)
                            if ubah >= 1 and ubah <= len(barang):
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
                        input("Tekan Enter...")

                    elif pilih == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== HAPUS BARANG ===")
                        for i in range(len(barang)):
                            print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
                        hapus = input("Pilih nomor barang: ")
                        if hapus.isdigit():
                            hapus = int(hapus)
                            if hapus >= 1 and hapus <= len(barang):
                                barang.pop(hapus-1)
                                print("Barang berhasil dihapus!")
                            else:
                                print("Nomor tidak ditemukan!")
                        else:
                            print("Masukkan angka!")
                        input("Tekan Enter...")

                    elif pilih == "5":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== DAFTAR USER ===")
                        for i in range(len(user)):
                            print(f"{i+1}. {user[i][0]} - {user[i][2]}")
                        input("Tekan Enter...")

                    elif pilih == "6":
                        menu_admin = False

            # USER
            else:
                menu_user = True
                while menu_user:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"=== MENU USER ({akun[0]}) ===")
                    print("1. Lihat Barang")
                    print("2. Beli Barang")
                    print("3. Lihat Keranjang & Bayar")
                    print("4. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== DAFTAR BARANG ===")
                        for i in range(len(barang)):
                            print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
                        input("Tekan Enter...")

                    elif pilih_user == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== BELI BARANG ===")
                        for i in range(len(barang)):
                            print(f"{i+1}. {barang[i][0]} - Rp{barang[i][1]}")
                        beli = input("Pilih nomor barang (0 batal): ")
                        if beli.isdigit():
                            beli = int(beli)
                            if beli == 0:
                                pass
                            elif beli >= 1 and beli <= len(barang):
                                keranjang.append(barang[beli-1])
                                print(f"{barang[beli-1][0]} ditambahkan ke keranjang!")
                            else:
                                print("Nomor barang tidak ada!")
                        else:
                            print("Masukkan angka!")
                        input("Tekan Enter...")

                    elif pilih_user == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=== KERANJANG BELANJA ===")
                        if len(keranjang) == 0:
                            print("Keranjang masih kosong!")
                        else:
                            total = 0
                            for i in range(len(keranjang)):
                                print(f"{i+1}. {keranjang[i][0]} - Rp{keranjang[i][1]}")
                                total += keranjang[i][1]
                            print("---------------------")
                            print(f"Total: Rp{total}")
                            print("---------------------")
                            bayar = input("Bayar sekarang? (y/n): ")
                            if bayar.lower() == "y":
                                print("Pembayaran berhasil! Terima kasih telah berbelanja.")
                                keranjang = []
                            else:
                                print("Pembayaran dibatalkan.")
                        input("Tekan Enter...")

                    elif pilih_user == "4":
                        menu_user = False

    # REGISTER
    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER AKUN ===")
        nama_baru = input("Masukkan username baru: ")
        sandi_baru = input("Masukkan password baru: ")
        ada = False
        for u in user:
            if u[0] == nama_baru:
                ada = True
        if ada:
            print("Username sudah digunakan!")
        else:
            user.append([nama_baru, sandi_baru, "user"])
            print("Akun berhasil dibuat!")
        input("Tekan Enter...")

    elif menu == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("Terima kasih telah berkunjung ke Toko Gaming!")
        menu_utama = False

    else:
        print("Pilihan tidak ada!")
        input("Tekan Enter...")
