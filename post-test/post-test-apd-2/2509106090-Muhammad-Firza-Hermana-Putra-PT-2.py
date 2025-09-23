nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")
harga = int(input("Masukkan harga menu makanan (Rp): "))

menu = {
    "Pecel Lele": 5,
    "Mie Ayam": 8,
    "Nasi Padang": 10
}

print(f"\n{nama} dengan NIM {nim} ingin membeli makanan seharga Rp {harga:,}\n")
print("="*60)
print(f"{'Menu':<15}{'Harga (Rp)':<15}{'Pajak (%)':<15}{'Total Bayar (Rp)':<15}")
print("="*60)

for makanan, pajak in menu.items():
    total = harga + (harga * pajak / 100)
    print(f"{makanan:<15}Rp {harga:<12,}% {pajak:<15}Rp {int(total):<12,}")

print("="*60)