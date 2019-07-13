import time
import os  # gatau buat apa awkoakoakakokawkaoawka

users = {
    "root": {
        "password": "bau-memec",
        "group": []
    }
}

point = 0

def soal1():
    correct_answer = "e"
    print('-'*30)
    print("1. Linux dibuat oleh ...")
    print("  a. Mark Zuckerberg")
    print("  b. Bill Gates")
    print("  c. Tim Berners Lee")
    print("  d. Atta Halilintar")
    print("  e. Linus Torvalds")
    jawaban1 = str(input("Jawaban > "))

    global point
    if jawaban1 == correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal2():
    correct_answer = "a"
    print("2. Siapa Founder Bahasa Pemrograman Python ?")
    print("  a. Guido Van Russom")
    print("  b. Tim Berners Lee")
    print("  c. Julian Assange")
    print("  d. Snowden")
    print("  e. Benjamin Engel")
    jawaban2 = str(input("Jawaban > "))

    global point
    if jawaban2 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal3():
    correct_answer = "c"
    print("3. Siapa Founder Sistem Operasi Microsoft ?")
    print("  a. Julian Assange")
    print("  b. Ria Ricis")
    print("  c. Bill Gates")
    print("  d. Tukang Pijat Nurhadi")
    print("  e. Tukang Sampah")
    jawaban3 = str(input("Jawaban > "))

    global point
    if jawaban3 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal4():
    correct_answer = "b"
    print("4. Nama Karakter utama di film Who Am I ?")
    print("  a. Kang Urut")
    print("  b. Benjamin Engel")
    print("  c. Bill Gates")
    print("  d. Nurhadi")
    print("  e. PELER")
    jawaban4 = str(input("Jawaban > "))

    global point
    if jawaban4 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal5():
    correct_answer = "b"
    print("5. Siapa Founder Apple ?")
    print("  a. Orang Kaya")
    print("  b. Steve Jobs")
    print("  c. Orang Missqueen")
    print("  d. Tukang Kebon")
    print("  e. Penulis Kode ini wkwk")
    jawaban5 = str(input("Jawaban > "))

    global point
    if jawaban5 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal6():
    correct_answer = "d"
    print("6. Bentuk Laptop ?")
    print("  a. Bulet kek muka lu wkwk")
    print("  b. Tissue")
    print("  c. Bintang")
    print("  d. Persegi Ajg")
    print("  e. ANJEUN ANJING PISAN WKWK")
    jawaban6 = str(input("Jawaban > "))

    global point
    if jawaban6 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal7():
    correct_answer = "c"
    print("7. Kapan Ngentot di lakukan ?")
    print("  a. Di Kebon")
    print("  b. Di Kamar Mandi")
    print("  c. Di kamar eue eue eue(jwbnnya ini ajg)")
    print("  d. Di Motor")
    print("  e. Di Mana terserah AJG")
    jawaban7 = str(input("Jawaban > "))

    global point
    if jawaban7 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal8():
    correct_answer = "a"
    print("8. Enakan Di Coliin apa Coli Sendiri ?")
    print("  a. DI COLIIN")
    print("  b. DI COLIIN AJG")
    print("  c. DI COLIIN MMQ")
    print("  d. DI COLIIN JMBD")
    print("  e. DI COLIIN PLEER")
    jawaban8 = str(input("Jawaban > "))

    global point
    if jawaban8 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal9():
    correct_answer = "b"
    print("9. Kapan Alwan Mendapatkan 5 Juta Rupiah dari Hasil Bug Bounty ?")
    print("  a. Taun Depan")
    print("  b. Hari ini ajg")
    print("  c. AKWOKAOKW")
    print("  d. Gatau wkwkwk")
    print("  e. Aing Tak Tau Ajg akwoakwoakwo")
    jawaban9 = str(input("Jawaban > "))

    global point
    if jawaban9 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal10():
    correct_answer = "e"
    print("10.bentuk ppq kek mana ")
    print("  a.lonjong ")
    print("  b.jajargenjang ")
    print("  c.kotak ")
    print("  d.Bulet ")
    print("  e.segitiga ")
    jawaban10 = str(input("Jawaban > "))

    global point
    if jawaban10 is correct_answer:
        time.sleep(1)
        print("Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def total_point():
    global point
    totalpoint = point
    print("Total Point Kamu Adalah: ", totalpoint)


def kumpulan_soal():
    soal1();
    soal2();
    soal3();
    soal4();
    soal5();
    soal6();
    soal7();
    soal8();
    soal9();
    soal10();
    total_point();

# INI NIH YANG MAISH BELUM JELAS JALAN KELUARNYA
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login sukses")
            return True
    return False

def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("username ga bole kosong ajg,isi la bgst")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("password ga boleh kosong anjg,isi la bgst")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password,buat akun dlu ppq kalo blm buat")

def daftar():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("username ga bole kosong ajg,isi la bgst")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("password ga bole kosong ajg,isi la bgst")
            continue
        else:
            break
    print("membuat akun ajg...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    time.sleep(1)
    print("akun sudah dibuat ppk,login menggunakan yg dibuat tadi")

def session(username):
    time.sleep(1)
    print("Welcome to system learning " + username)
    print("Options: [1.]Soal | [q.]Quit")
    while True:
        input_user = input(username + " > ")
        if input_user == "1":
            kumpulan_soal()

        elif input_user == "q":
            exit()

        else:
            print(input_user + "\nyg bener inputnya gblk")
            


# DI BAWAH INI YANG BAKAL PERTAMA KALI TAMPIL JMBUD
def menu():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+              Welcome to the system learning            +")
    print("+             sebelum login daftar dlu ya ajg          +")
    print("+         Options: [1.].login | [2.].Daftar |[9].exit    +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    start = 0

    while start != 10:

        input_user = str(input('pilih angka > '))

        if input_user == "1":
            login()

        elif input_user == "2":
            daftar()

        elif input_user == "9":
            exit()

        else:
            print(input_user + "\nyg bener inputnya gblk")


menu()
