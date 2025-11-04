from data import barang, keranjang, total_penjualan
from prettytable import PrettyTable

def menu_user(nama):
    global total_penjualan
    while True:
        print(f"=== MENU USER ===")
        print("1. Lihat Barang")
        print("2. Beli Barang")
        print("3. Lihat Keranjang & Bayar")
        print("4. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            table = PrettyTable(["Kode","Nama","Harga","Stok","Kategori"])
            for k,v in barang.items():
                table.add_row([k,v["nama"],v["harga"],v["stok"],v["kategori"]])
            print(table)
            input("ENTER...")

        elif pilih == "2":
            kode = int(input("Kode barang: "))
            if kode in barang:
                if barang[kode]["stok"]>0:
                    keranjang.append(barang[kode])
                    barang[kode]["stok"]-=1
                    print("ditambahkan ke keranjang!")
                else:
                    print("stok habis")
            else:
                print("kode tidak ada")
            input("ENTER...")

        elif pilih == "3":
            if not keranjang:
                print("keranjang kosong")
            else:
                total = sum(item["harga"] for item in keranjang)
                table = PrettyTable(["No","Nama","Harga"])
                for i,item in enumerate(keranjang,1):
                    table.add_row([i,item["nama"],item["harga"]])
                print(table)
                print(f"TOTAL = Rp{total}")
                bayar = input("bayar? (ya/tidak): ")
                if bayar.lower()=="ya":
                    total_penjualan += total
                    keranjang.clear()
                    print("Pembayaran berhasil")
            input("ENTER...")

        elif pilih == "4":
            break

        else:
            print("pilihan tidak ada")
