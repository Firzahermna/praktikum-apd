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
total_penjualan = 0

def clear():
    os.system("cls")

def tampilkan_barang():
    print("========== DAFTAR BARANG ==========")
    for kode, info in barang.items():
        status = "Habis" if info["stok"] == 0 else f"{info['stok']} stok"
        print(f"{kode}. {info['nama']} - Rp{info['harga']} | {status} | Kategori: {info['kategori']}")
