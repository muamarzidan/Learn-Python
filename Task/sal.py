def fungsiview():
#menampilkan isi data dalam tabel
#fetchall () : untuk mengambil seluruh data
#fetchmany(3) : untuk mengambil beberaoa data (sesuai parameter)
#fetchome () : untuk mengambil satu data diawal
#fungsi-fungsi akan mengembalikan data list yang berisi record/tuple
    import mysql.connector

    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        db = "dbbuku"

    )

    dbcursor = con.cursor()
    sql = "select * from buku"
    dbcursor.execute(sql)
    dt = dbcursor.fetchall()

    for data in dt:
        print(data)

def fungsiupdate():
    import mysql.connector

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="dbbuku"

    )

    if con.is_connected():
        print("Update Data Behasil")

    dbcursor = con.cursor()
    sql = "update buku set kode_buku=%s, judul_buku=%s, penulis_buku=%s, penerbit_buku=%s, tahun_penerbit=%s, stok=%s where id_buku=%s"
    data = "3614", "Rumah Hantu", "Jojon", "Gramedia", "2021", "12", "0005"
    dbcursor.execute(sql, data)

    con.commit()

    import mysql.connector

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="dbbuku"

    )

    dbcursor = con.cursor()
    sql = "insert into buku (id_buku,kode_buku,judul_buku,penulis_buku,penerbit_buku,tahun_penerbit,stok) values(%s,%s,%s,%s,%s,%s,%s)"
    data = ("0001", "3104", "Laskar Pelangi", "Andrea Hirata", "Gramedia", "2010", "10")

    dbcursor.execute(sql, data)
    con.commit()

    print("Data berhasil disimpan")

def fungsiinsert():
    import mysql.connector

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",

    )

    if con.is_connected():
        print("koneksi ke server database berhasil")

    db = con.cursor()
    db.execute("create database dbbuku")

def fungsidelete():
    import mysql.connector

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="dbbuku"

    )

    if con.is_connected():
        print("Hapus Data Berhasil")

    dbcursor = con.cursor()
    sql = "delete from buku where kode_buku = '3614'"
    dbcursor.execute(sql)

    con.commit()

def fungsibuat():
    import mysql.connector

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",

    )

    if con.is_connected():
        print("koneksi ke server database berhasil")

    db = con.cursor()
    db.execute("create database dbbuku")

def fungsimenu():
    print("1. fungsiview")
    print("2. fungsiupdate")
    print("3. fungsiinsert")
    print("4. fungsidelete")
    print("5. fungsibuat")
    pilih = int(input("Masukan Pilihan Menu: "))

    if pilih == 1:
        fungsiview()

    elif pilih == 2:
        fungsiupdate()

    elif pilih == 3:
        fungsiinsert()

    elif pilih == 4:
        fungsidelete()

    elif pilih == 5:
        fungsibuat()

    fungsimenu()

def ulang():
    x = 0
    while x == 0:
        pilih = input("Mau Run Lagi? (y/t) : ")
        if pilih == "y" or pilih == "Y":
            fungsimenu()
        elif pilih == "t" or pilih == "T":
            print("Prgoram Ditutup")
            break
        else:
            print("Silahkan Pilih Menu")

ulang()