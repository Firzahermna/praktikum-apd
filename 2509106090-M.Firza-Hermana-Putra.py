import os

users = {
    "admin": {"password": "123", "role": "admin"},
    "firza": {"password": "090", "role": "user"}
}

barang = {
    1: {"nama": "Keyboard Logitech", "harga": 500000, "stok": 10, "kategori": "Periferal"},
    2: {"nama": "Item Wibu", "harga": 400000, "stok": 0, "kategori": "Aksesoris"},
    3: {"nama": "Meja Gaming RGB", "harga": 5000000, "stok": 3, "kategori": "Furniture"},
    4: {"nama": "Mouse INNO X3", "harga": 410000, "stok": 8, "kategori": "Periferal"},
    5: {"nama": "Headset Rexus HX20", "harga": 300000, "stok": 6, "kategori": "Audio"},
    6: {"nama": "Kursi Gaming biar nyaman 1", "harga": 1500000, "stok": 4, "kategori": "Furniture"},
    7: {"nama": "Mic biar ga apakali itu suara", "harga": 850000, "stok": 5, "kategori": "Audio"},
    8: {"nama": "Monitor kaciw 9000hz", "harga": 900000000, "stok": 1, "kategori": "Display"}
    
}

keranjang = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_barang():
    print("=== DAFTAR BARANG ===")
    for kode, info in barang.items():
        status = "Habis" if info["stok"] == 0 else f"{info['stok']} stok"
        print(f"{kode}. {info['nama']} - Rp{info['harga']} | {status} | Kategori: {info['kategori']}")

menu_utama = True
while menu_utama:
    clear()
    print("=== TOKO PERALATAN GAMING ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        clear()
        print("=== LOGIN ===")
        nama = input("Masukkan username: ")
        sandi = input("Masukkan password: ")

        if nama in users and users[nama]["password"] == sandi:
            print("Login berhasil!")
            input("Tekan Enter untuk lanjut...")
            role = users[nama]["role"]

            if role == "admin":
                menu_admin = True
                while menu_admin:
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
                        tampilkan_barang()
                        input("Tekan Enter...")

                    elif pilih == "2":
                        clear()
                        print("=== TAMBAH BARANG ===")
                        nama_brg = input("Nama barang: ")
                        harga_brg = input("Harga barang: ")
                        stok_brg = input("Stok barang: ")
                        kategori_brg = input("Kategori barang: ")
                        if harga_brg.isdigit() and stok_brg.isdigit():
                            kode_baru = max(barang.keys()) + 1
                            barang[kode_baru] = {
                                "nama": nama_brg,
                                "harga": int(harga_brg),
                                "stok": int(stok_brg),
                                "kategori": kategori_brg
                            }
                            print("Barang berhasil ditambah!")
                        else:
                            print("Harga dan stok harus berupa angka!")
                        input("Tekan Enter...")

                    elif pilih == "3":
                        clear()
                        tampilkan_barang()
                        ubah = input("Pilih kode barang: ")
                        if ubah.isdigit():
                            ubah = int(ubah)
                            if ubah in barang:
                                nama_baru = input("Nama baru: ")
                                harga_baru = input("Harga baru: ")
                                stok_baru = input("Stok baru: ")
                                kategori_baru = input("Kategori baru: ")
                                if harga_baru.isdigit() and stok_baru.isdigit():
                                    barang[ubah] = {
                                        "nama": nama_baru,
                                        "harga": int(harga_baru),
                                        "stok": int(stok_baru),
                                        "kategori": kategori_baru
                                    }
                                    print("Barang berhasil diubah!")
                                else:
                                    print("Harga dan stok harus angka!")
                            else:
                                print("Kode tidak ditemukan!")
                        else:
                            print("Masukkan angka!")
                        input("Tekan Enter...")

                    elif pilih == "4":
                        clear()
                        tampilkan_barang()
                        hapus = input("Pilih kode barang: ")
                        if hapus.isdigit():
                            hapus = int(hapus)
                            if hapus in barang:
                                del barang[hapus]
                                print("Barang berhasil dihapus!")
                            else:
                                print("Kode tidak ditemukan!")
                        else:
                            print("Masukkan angka!")
                        input("Tekan Enter...")

                    elif pilih == "5":
                        clear()
                        print("=== DAFTAR USER ===")
                        for i, (u, info) in enumerate(users.items(), 1):
                            print(f"{i}. {u} - {info['role']}")
                        input("Tekan Enter...")

                    elif pilih == "6":
                        menu_admin = False

            else:
                menu_user = True
                while menu_user:
                    clear()
                    print(f"=== MENU USER ({nama}) ===")
                    print("1. Lihat Barang")
                    print("2. Beli Barang")
                    print("3. Lihat Keranjang & Bayar")
                    print("4. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        clear()
                        tampilkan_barang()
                        input("Tekan Enter")

                    elif pilih_user == "2":
                        clear()
                        tampilkan_barang()
                        beli = input("Pilih kode barang (0 untuk batal): ")
                        if beli.isdigit():
                            beli = int(beli)
                            if beli == 0:
                                pass
                            elif beli in barang:
                                if barang[beli]["stok"] > 0:
                                    keranjang.append(barang[beli])
                                    barang[beli]["stok"] -= 1
                                    print(f"{barang[beli]['nama']} ditambahkan ke keranjang!")
                                else:
                                    print("Stok barang habis!")
                            else:
                                print("Kode barang tidak ada!")
                        else:
                            print("Masukkan angka!")
                        input("Tekan Enter...")

                    elif pilih_user == "3":
                        clear()
                        print("=== KERANJANG BELANJA ===")
                        if not keranjang:
                            print("Keranjang masih kosong.")
                        else:
                            total = 0
                            for i, item in enumerate(keranjang, 1):
                                print(f"{i}. {item['nama']} - Rp{item['harga']}")
                                total += item["harga"]
                            print("---------------------")
                            print(f"Total: Rp{total}")
                            print("---------------------")
                            bayar = input("Bayar sekarang? (y/n): ")
                            if bayar.lower() == "y":
                                print("Pembayaran berhasil! Terima kasih telah berbelanja ")
                                keranjang.clear()
                            else:
                                print("Pembayaran dibatalkan.")
                        input("Tekan Enter...")

                    elif pilih_user == "4":
                        menu_user = False

        else:
            print("Username atau password salah!")
            input("Tekan Enter...")

    elif menu == "2":
        clear()
        print("=== REGISTER AKUN ===")
        nama_baru = input("Masukkan username baru: ")
        sandi_baru = input("Masukkan password baru: ")
        if nama_baru in users:
            print("Username sudah digunakan!")
        elif nama_baru == "" or sandi_baru == "":
            print("Username dan password tidak boleh kosong!")
        else:
            users[nama_baru] = {"password": sandi_baru, "role": "user"}
            print("Akun berhasil dibuat!")
        input("Tekan Enter...")

    elif menu == "3":
        clear()
        print("Terima kasih telah berkunjung ke Toko Gaming ")
        menu_utama = False

    else:
        print("Pilihan tidak ada!")
        input("Tekan Enter...")
