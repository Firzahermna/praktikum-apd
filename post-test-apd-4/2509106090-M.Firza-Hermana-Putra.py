# ===============================
# Program Pembelian Tiket Bioskop XX0
# ===============================

# Data login
USERNAME = "Firza"
PASSWORD = "2509106090"  


login_berhasil = False
percobaan = 0
MAKSIMAL_LOGIN = 3

while percobaan < MAKSIMAL_LOGIN:
    print("\n=== LOGIN BIOSKOP XX0 ===")
    input_user = input("Masukkan Username: ")
    input_pass = input("Masukkan NIM: ")

    if input_user == USERNAME and input_pass == PASSWORD:
        print("\nLogin berhasil!\n")
        login_berhasil = True
        break
    else:
        percobaan += 1
        print(f"Login gagal! Percobaan ke-{percobaan}\n")

if not login_berhasil:
    print("Gagal login 3 kali. Program dihentikan.")
    exit()



def tampilkan_menu():
    print("=== MENU PEMBELIAN TIKET BIOSKOP XX0 ===")
    print("1. Tiket Reguler - Rp 50.000")
    print("2. Tiket VIP     - Rp100.000")
    print("3. Tiket VVIP    - Rp150.000")
    print("4. Keluar")
    print("========================================")

while True:
    tampilkan_menu()
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        jenis_tiket = "Reguler"
        harga_tiket = 50000
    elif pilihan == "2":
        jenis_tiket = "VIP"
        harga_tiket = 100000
    elif pilihan == "3":
        jenis_tiket = "VVIP"
        harga_tiket = 150000
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan Bioskop XX0.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-4.\n")
        continue

    jumlah_input = input(f"Masukkan jumlah tiket {jenis_tiket} yang ingin dibeli: ")

    if not jumlah_input.isdigit():
        print("Jumlah tiket harus berupa angka.\n")
        continue

    jumlah_tiket = int(jumlah_input)

    if jumlah_tiket <= 0:
        print("Jumlah tiket minimal 1.\n")
        continue


    total_bayar = 0
    for i in range(jumlah_tiket):
        total_bayar += harga_tiket


    potongan = 0
    bonus = ""

    if total_bayar >= 300000:
        potongan = total_bayar * 0.12
    elif total_bayar >= 200000:
        potongan = total_bayar * 0.08
    elif total_bayar >= 150000:
        bonus = "Poster Film Eksklusif"

    total_setelah_diskon = total_bayar - potongan


    print("\n====== RINCIAN PEMBELIAN ======")
    print(f"Jenis Tiket    : {jenis_tiket}")
    print(f"Jumlah Tiket   : {jumlah_tiket}")
    print(f"Total Bayar    : Rp{total_bayar:,}")

    if potongan > 0:
        print(f"Potongan       : Rp{int(potongan):,}")
        print(f"Total Akhir    : Rp{int(total_setelah_diskon):,}")
    else:
        print(f"Total Akhir    : Rp{total_bayar:,}")

    if bonus != "":
        print(f"Bonus          : {bonus}")
    print("================================\n")