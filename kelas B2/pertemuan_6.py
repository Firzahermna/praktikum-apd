# # # # # # # buah = {"apel", "naga", "mangga", "apel"}
# # # # # # # print(buah)

# # # # # # angka_ganjil = {}

# # # # # Daftar_buku = {
# # # # # "Buku1" : "Bumi Manusia",
# # # # # "Buku2" : "Laut Bercerita"
# # # # # }

# # # # # print(Daftar_buku["Buku1"])
# # # # # print(Daftar_buku)

# # # # Biodata = {
# # # # "Nama" : "Ananda Daffa Harahap",
# # # # "NIM" : 2409106050,
# # # # "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"].
# # # # "Mahasiswa_Aktif" : True,
# # # # "Social Media" : {"Instagram" : "daffahrhap"
# # # # }
# # # # }


# # # list_mahasiswam = dict(nama="dapupu", jurusan="informatika")
# # # print(list_mahasiswam)

# # # Nilai = {
# # # "Matematika": 80,
# # # "B. Indonesia": 90,
# # # "B. Inggris": 81,
# # # "Kimia": 78,
# # # "Fisika": 80
# # # }
# # # # Tanpa menggunakan items()
# # # for i in Nilai:
# # #     print(i)
# # # print("") # pemisah
# # # # Menggunakan items()
# # # for i, j in Nilai.items():
# # #     print(f"Nilai {i} anda adalah {j}")
# # # # # output
# # # # Matematika
# # # # B. Indonesia
# # # # B. Inggris
# # # # Kimia
# # # # Fisika
# # # # Nilai Matematika anda adalah 80
# # # # Nilai B. Indonesia anda adalah 90
# # # # Nilai B. Inggris anda adalah 81
# # # # Nilai Kimia anda adalah 78
# # # # Nilai Fisika anda adalah 80


# # Film = {
# # "Avenger Endgame" : "Action",
# # "Sherlock Holmes" : "Mystery",
# # "The Conjuring" : "Horror"
# # }
# # #Sebelum Ditambah
# # print(Film)
# # Film["Zombieland"] = "Comedy"
# # Film.update({"Hours" : "Thriller"})
# # print("")

# # print("filem di tambah")
# # print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'}
# {'Umur': 19, 'Jurusan': 'Informatika'}
# None


data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
cache = data.pop("Nama")
#Setelah dihapus
print(data)
#memanggil data yang telah dihapus pada dictionary
print(data.get("Nama"))
#memanggil data yang telah dihapus pada variabel cache
print(cache)
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'}
{'Umur': 19, 'Jurusan': 'Informatika'}

