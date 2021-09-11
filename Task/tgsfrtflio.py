print("~~~PROGRAM KASIR TOKO KASET~~~")
pembeli = input("masukan nama pembeli : ")
print("Nama Pembeli : ", pembeli)

total1 = 0
jenis1 = ""
kaset = 0
kaset = 0
total12 = 0
jenis2 = ""

def fungsikasetmusik():
    global total1
    global kaset
    global jenis1
    print("\n~~~~Daftar Kaset Musik~~~~")
    print("1. Dangdut Rhoma irama full album - Rp.15000")
    print("2. lagu via vallen full album - Rp.15000")
    print("3. Neffex full song  - Rp.13000")
    nomor = int(input("Masukan Pilihan: "))
    kaset = int(input("Berapa Kaset: "))

    if nomor == 1:
        total1 = kaset * 15000
        print(kaset, "Dangdut Rhoma irama full album = Rp", total1)
        jenis1 = ("Dangdut Rhoma irama full album")
    elif nomor == 2:
        total1 = kaset * 15000
        print(kaset, "lagu via vallen full album  = Rp", total1)
        jenis1 = ("lagu via vallen full album")
    elif nomor == 3:
        total1 = kaset * 13000
        print(kaset, "Neffex full song = Rp", total1)
        jenis1 = ("Neffex full song")
    else:
        print("Pilihan tidak ada,silahkan masuk lagi")
        fungsikasetmusik()

def fungsikasetfilm():
    global total2
    global jenis2
    global kaset
    print("\n~~~~Daftar Kaset Film~~~~")
    print("1. One piece movie stampede - Rp20000")
    print("2. Power ranger - Rp20000")
    print("3. Attack on titan movie rumbling - Rp25000")
    nomor = int(input("Masukan Pilihan: "))
    kaset = int(input("Berapa Kaset: "))

    if nomor == 1:
        total2 = kaset * 20000
        print(kaset, " One piece movie stampede = Rp", total2)
        jenis2 = ("Kaset one piece movie stampede")
    elif nomor == 2:
        total2 = kaset * 20000
        print(kaset, " Power ranger = Rp", total2)
        jenis2 = ("Kaset power ranger")
    elif nomor == 3:
        total2 = kaset * 25000
        print(kaset, " Attack on titan movie rumbling = Rp", total2)
        jenis2 = ("Attack on titan movie rumbling")
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        fungsikasetfilm()

def ulang():
    x = 0
    while x == 0:
        pilih = input("Transaksi Lagi (y/t) : ")
        if pilih == "y" or pilih == "Y":
            programkasir()
        elif pilih == "t" or pilih == "T":
            print("Terima Kasih sudah membeli di toko kami")
            break
        else:
             print("Selamat Menikmati")

def programkasir():
    fungsikasetmusik()
    fungsikasetfilm()

    totalsemua = 0
    totalsemua = total1 + total2
    print("\nTotal harus Dibayar: Rp", totalsemua)
    uang = int(input("Uang Tunai Pembeli: Rp."))
    kembalian = int(uang - totalsemua)
    print("Kembalian :", kembalian)
    print("\n==========================================")
    print("========== S T R U K B E L I ==========")
    print("==========================================")
    print(" Nama :", pembeli)
    print(" Beli :", kaset, jenis1, "-", total1)
    print(" ", kaset, jenis2, "-", total2)
    print(" Tagihan : Rp.", totalsemua)
    print(" Uang : Rp.", uang)
    print(" Kembalian : Rp.", kembalian)
    print("==========================================")
    print("==========================================")
    ulang()

programkasir()
