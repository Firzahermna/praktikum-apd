import random
import time
import os

# Data ikan berdasarkan tier
fish_list = [
    {"name": "Ikan Biasa", "chance": 0.6, "value": 10, "tier": "Biasa"},
    {"name": "Ikan Langka", "chance": 0.25, "value": 40, "tier": "Langka"},
    {"name": "Ikan Legendaris", "chance": 0.1, "value": 120, "tier": "Legendaris"},
    {"name": "Ikan Rahasia", "chance": 0.05, "value": 300, "tier": "Rahasia"}
]

# Data player
player = {
    "name": "Pemancing",
    "money": 0,
    "rod_level": 1,
    "inventory": {}  # menyimpan jumlah per jenis ikan
}

is_day = True
auto_fishing = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def change_time():
    global is_day
    is_day = not is_day
    waktu = "🌞 Siang" if is_day else "🌙 Malam"
    print(f"\nWaktu berganti menjadi {waktu}.")
    time.sleep(1)

def fishing():
    global is_day
    print("\n🎣 Melempar kail...")
    time.sleep(1)
    print("Menunggu ikan menggigit...")
    time.sleep(1)

    roll = random.random()
    chance_boost = player["rod_level"] * 0.05
    time_boost = 0.05 if is_day else -0.02

    caught = None
    for fish in fish_list:
        if roll < fish["chance"] + chance_boost + time_boost:
            caught = fish
            break

    if caught:
        name = caught["name"]
        player["inventory"][name] = player["inventory"].get(name, 0) + 1
        print(f"🐟 Kamu menangkap {name}! ({caught['tier']})")
    else:
        print("❌ Tidak ada ikan yang didapat kali ini.")

def sell_fish():
    if not player["inventory"]:
        print("🪹 Kamu belum punya ikan untuk dijual!")
        return
    total = 0
    for fish in fish_list:
        name = fish["name"]
        if name in player["inventory"]:
            total += fish["value"] * player["inventory"][name]
    player["money"] += total
    print(f"💰 Kamu menjual semua ikan seharga {total} koin!")
    player["inventory"].clear()

def upgrade_rod():
    cost = player["rod_level"] * 100
    if player["money"] >= cost:
        player["money"] -= cost
        player["rod_level"] += 1
        print(f"🔥 Pancinganmu naik ke level {player['rod_level']}!")
    else:
        print(f"❌ Uangmu tidak cukup! Butuh {cost} koin.")

def show_stats():
    print("\n=== Statistik Pemancing ===")
    print(f"Nama: {player['name']}")
    print(f"Uang: {player['money']}")
    print(f"Level Pancing: {player['rod_level']}")
    print(f"Waktu: {'Siang 🌞' if is_day else 'Malam 🌙'}")
    print("===========================\n")

def show_inventory():
    if not player["inventory"]:
        print("🪹 Inventorimu kosong.")
        return
    print("\n=== 🎒 INVENTORI IKAN ===")
    total = 0
    for fish in fish_list:
        name = fish["name"]
        if name in player["inventory"]:
            jumlah = player["inventory"][name]
            tier = fish["tier"]
            value = fish["value"]
            print(f"{name:<15} | Tier: {tier:<10} | Jumlah: {jumlah:<3} | Nilai: {value} koin")
            total += jumlah
    print(f"Total Ikan: {total}")
    print("===========================\n")

def shop():
    while True:
        print("\n=== 🏪 SHOP ===")
        print("1. Upgrade Pancing")
        print("2. Kembali ke Menu Utama")
        pilih = input("Pilih: ")
        if pilih == "1":
            upgrade_rod()
        elif pilih == "2":
            print("Kembali ke menu utama...")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid!")

def auto_fish():
    global auto_fishing
    if auto_fishing:
        print("⚠️ Auto pancing sudah aktif!")
        return
    auto_fishing = True
    print("\n🔁 Auto Pancing dimulai! Gunakan menu 'Stop Auto' untuk berhenti.")
    while auto_fishing:
        fishing()
        time.sleep(1.5)

def stop_auto():
    global auto_fishing
    if not auto_fishing:
        print("❌ Auto pancing belum aktif!")
    else:
        auto_fishing = False
        print("🛑 Auto Pancing dihentikan!")

# Main loop
while True:
    print("=== 🎣 Game Fish It Deluxe ===")
    print("1. Pancing Ikan")
    print("2. Auto Pancing")
    print("3. Stop Auto")
    print("4. Jual Ikan")
    print("5. Lihat Inventori")
    print("6. Lihat Statistik")
    print("7. Ganti Siang/Malam")
    print("8. Shop")
    print("9. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        fishing()
    elif pilihan == "2":
        auto_fish()
    elif pilihan == "3":
        stop_auto()
    elif pilihan == "4":
        sell_fish()
    elif pilihan == "5":
        show_inventory()
    elif pilihan == "6":
        show_stats()
    elif pilihan == "7":
        change_time()
    elif pilihan == "8":
        shop()
    elif pilihan == "9":
        print("Terima kasih sudah bermain!")
        break
    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk lanjut...")
    clear()
