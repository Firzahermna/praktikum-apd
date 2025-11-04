from data import users
from admin import menu_admin
from user import menu_user

def login():
    print("=== LOGIN ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil!")

        role = users[username]["role"]

        if role == "admin":
            menu_admin()
        else:
            menu_user(username)
    else:
        print("Username / Password salah!")
