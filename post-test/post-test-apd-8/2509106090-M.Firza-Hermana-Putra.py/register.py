from data import users

def register():
    print("=== REGISTER ===")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    if username in users:
        print("Username sudah digunakan!")
    elif username == "" or password == "":
        print("Username & password tidak boleh kosong!")
    else:
        users[username] = {"password": password, "role": "user"}
        print("Akun berhasil dibuat!")
