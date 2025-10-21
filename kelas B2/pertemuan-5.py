# mahasigma = ["zuhri", "rizal", 23, 0.45,
#              ["iza", 12]]
# print(mahasigma )

# # list awal
# mahasigma = ["andi", "budi", 23, 0.45,
#              ["pernan", 12, ["for real", ["adit"]]]]
# # Tambahkan Web
# mahasigma[4][2][1][0] = ["dapupu", "pernan"]
# mahasigma.append("siapa ya")

# print(mahasigma)


# #cara menghapus di salah satu list del
# anakB2 = ['julpa', 'dono', 'zuhri','for real']
# print(anakB2)
# del anakB2[2]

# # print(anakB2)

# #cara menghapus di salah satu list remov
# anakB2 = ['julpa', 'dono', 'zuhri','for real']
# print(anakB2)
# anakB2.remove("zuhri")

# print(anakB2)

import time
import os
import sys

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def slide_in_text(text, width=60, delay_slide=0.02):
    # slide dari kanan: dari indentasi besar ke 0
    for spaces in range(width, -1, -2):
        clear_console()
        print(" " * spaces + text)
        time.sleep(delay_slide)

def type_text(text, delay=0.1):
    out = ""
    for ch in text:
        out += ch
        clear_console()
        print(out)
        time.sleep(delay)

def animate_line(text):
    slide_in_text(text, width=60, delay_slide=0.01)
    type_text(text, delay=0.07)
    time.sleep(0.5)

def main():
    lines = [
        "Tante...",
        "Sudah terbiasa terjadi tante...",
        "Teman datang cuma kalo butuh saja...",
        "Coba kalau lagi susah...",
        "Mereka semua menghilaaaang..."
    ]
    for line in lines:
        animate_line(line)
    print("\n🎶 Selesai")

if __name__ == "__main__":
    main()
