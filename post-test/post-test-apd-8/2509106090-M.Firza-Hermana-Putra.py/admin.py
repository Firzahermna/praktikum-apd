from data import barang, users, total_penjualan
from prettytable import PrettyTable

def menu_admin():
    while True:
        print("=== MENU ADMIN ===")
        print("1. Lihat Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Lihat User")
        print("6. Pendapatan Toko")
        print("7. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            table = PrettyTable(["Kode", "Nama", "Harga", "Stok", "Kategori"])
            for k,v in barang.items():
                table.add_row([k,v["nama"],v["harga"],v["stok"],v["kategori"]])
            print(table)
            input("ENTER...")

        elif pilih == "2":
            nama = input("Nama barang: ")
            harga = input("Harga: ")
            stok = input("Stok: ")
            kategori = input("Kategori: ")
            if harga.isdigit() and stok.isdigit():
                kode_baru = max(barang.keys())+1
                barang[kode_baru]={ "nama":nama,"harga":int(harga),"stok":int(stok),"kategori":kategori}
                print("Barang berhasil ditambah!")
            else:
                print("harga & stok wajib angka")
            input("ENTER...")

        elif pilih == "3":
            kode = int(input("Pilih kode barang: "))
            if kode in barang:
                nama = input("Nama baru: ")
                harga = input("Harga baru: ")
                stok = input("Stok baru: ")
                kategori = input("Kategori baru: ")
                if harga.isdigit() and stok.isdigit():
                    barang[kode]={ "nama":nama,"harga":int(harga),"stok":int(stok),"kategori":kategori}
                    print("Barang berhasil diubah!")
                else:
                    print("Harga & stok harus angka!")
            else:
                print("kode tidak ditemukan")
            input("ENTER...")

        elif pilih == "4":
            kode = int(input("Pilih kode barang: "))
            if kode in barang:
                del barang[kode]
                print("barang dihapus")
            else:
                print("kode tidak ada")
            input("ENTER...")

        elif pilih == "5":
            table = PrettyTable(["No","Username","Role"])
            i=1
            for u,v in users.items():
                table.add_row([i,u,v["role"]])
                i+=1
            print(table)
            input("ENTER...")

        elif pilih == "6":
            print(f"Total pendapatan toko: Rp{total_penjualan}")
            input("ENTER...")

        elif pilih == "7":
            break

        else:
            print("pilihan tidak ada")
