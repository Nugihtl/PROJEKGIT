# Nugra Hasahatan Lubis
# 2403457
# RPL 1 B

def login():
    username = "Daspro2023"
    password = "Latihan"
    kesempatan = 3
    percobaan = 0
    
    print("Silahkan login")
    
    while percobaan < kesempatan:
        input_username = input("Masukkan username: ")
        input_password = input("Masukkan password: ")
        
        if input_username==username and input_password==password:
            print("Login berhasil, selamat datang, Admin!")
            return
        elif input_password == password:
            print(f"Login berhasil, selamat datang {input_username}")
            return
        else:
            percobaan += 1
            print(f"Login gagal kesempatan anda tersisa {kesempatan - percobaan}x")
    
    print("Kesempatan anda sudah habis. Akses ditolak.")
    return

login()
