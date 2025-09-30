nama_asli = "Firza"
nim_asli = "06090"
biaya_langganan = 1500000

print("=== LOGIN DULU ===")
nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM  : ")

if nama == nama_asli and nim == nim_asli:
    print("\nLogin Berhasil!\n")
    print("\n=== PILIH PAKET LANGGANAN ===\n")
    print("1. Bronze (Admin 1%) -> Akses dasar ke lagu-lagu populer")
    print("2. Silver (Admin 3%) -> Akses lagu premium dan playlist kustom")
    print("3. Gold (Admin 5%)   -> Akses lagu premium, playlist kustom, dan mode offline")
    print("4. Platinum (Admin 7%) -> Akses semua fitur, playlist kustom, mode offline, konten eksklusif artis")

    pilihan = input("\nMasukkan pilihan paket (1-4): ")

    if pilihan == "1":
        admin = 0.01
        paket = "Bronze"
        fitur = "Akses dasar ke lagu-lagu populer"
    elif pilihan == "2":
        admin = 0.03
        paket = "Silver"
        fitur = "Akses lagu premium dan playlist kustom"
    elif pilihan == "3":
        admin = 0.05
        paket = "Gold"
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan == "4":
        admin = 0.07
        paket = "Platinum"
        fitur = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        print("Pilihan tidak tidak ada")
        exit()

    biaya_admin = biaya_langganan * admin
    total_bayar = biaya_langganan + biaya_admin

    print("\n=== DETAIL PEMBAYARAN ===")
    print("Paket          :", paket)
    print("Biaya Dasar    : Rp", biaya_langganan)
    print("Biaya Admin    : Rp", int(biaya_admin))
    print("Total Bayar    : Rp", int(total_bayar))
    print("Keuntungan     :", fitur)

else:
    print("\nLogin Gagal Nama atau NIM salah.")