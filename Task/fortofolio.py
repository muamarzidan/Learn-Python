print("~~~COFFE KUY~~~")
pembeli = input("masukan nama pembeli : ")
print("nama Pembeli : ", pembeli)

total1 = 0
jenis1 = ""
porsi = 0
Gelas = 0
total12 = 0
jenis2 = ""

def fungsiminuman():
    global total1
    global porsi
    global jenis1
    print("\n~~~~Menu Coffe~~~~")
    print("1. Kopi Seruput - Rp.10000")
    print("2. Kopi Hitam - Rp.9000")
    print("3. Es Kopi Susu  - Rp.14000")
    print("4. Es Kopi Latte  - Rp.15000")
    print("5. Es Kopi Redvelvet  - Rp.120000")
    nomor = int(input("Masukan Pilihan: "))
    Gelas =int(input("Berapa Gelas: "))

    if nomor == 1:
        total1 = Gelas * 10000
        print(Gelas, "Gelas Kopi Seruput = Rp", total1)
        jenis1 = ("Kopi Seruput")
    elif nomor == 2:
        total1 = Gelas * 9000
        print(Gelas, "Gelas Kopi Hitam  = Rp", total1)
        jenis1 = ("Kopi Hitam")
    elif nomor == 3:
        total1 = Gelas * 14000
        print(Gelas, "Gelas Es Kopi Susu = Rp", total1)
        jenis1 = ("Es Kopi Susu")
    elif nomor == 4:
        total1 = Gelas * 15000
        print(Gelas, "Gelas Es Kopi Latte = Rp", total1)
        jenis1 = ("Es Kopi Latte")
    elif nomor == 5:
        total1 = Gelas * 120000
        print(Gelas, "Gelas Es Kopi Redvelvet = Rp", total1)
        jenis1 = ("Es Kopi Redvelvet")
    else:
        print("Pilihan tidak ada,silahkan masuk lagi")
        fungsiminuman()

def fungsicemilan():
    global total2
    global jenis2
    global gelas
    print("\n~~~~Menu Cemilan~~~~")
    print("1. Roti Bakar Susu - Rp12000")
    print("2. Kentang Goreng - Rp9000")
    print("3. Sandwich - Rp16000")
    nomor = int(input("Masukan Pilihan: "))
    Porsi = int(input("Berapa Porsi: "))

    if nomor == 1:
        total2 = Porsi * 12000
        print(Porsi, " Roti Bakar Susu = Rp", total2)
        jenis2 = (" Roti Bakar Susu")
    elif nomor == 2:
        total2 = Porsi * 9000
        print(Porsi, " kentang Goreng = Rp", total2)
        jenis2 = ("Kentang Goreng")
    elif nomor == 3:
        total2 = Porsi * 16000
        print(Porsi, " Sandwich = Rp", total2)
        jenis2 = ("Sandwich")
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        fungsicemilan()

def ulang():
    x = 0
    while x == 0:
        pilih = input("Transaksi Lagi (y/t) : ")
        if pilih == "y" or pilih == "Y":
            programkasir()
        elif pilih == "t" or pilih == "T":
            print("Terima Kasih sudah membeli di COFFE KUY")
            break
        else:
             print("Selamat Menikmati")

def programkasir():
    fungsiminuman()
    fungsicemilan()

    totalsemua = total1 + total2
    print("\nTotal harus Dibayar: Rp", totalsemua)
    uang = int(input("Uang Tunai Pembeli: Rp."))
    kembalian = int(uang - totalsemua)
    print("Kembalian :", kembalian)
    print("\n===============================================")
    print("========== S T R U K P E M B E L I A N ==========")
    print("=================================================")
    print(" Nama :", pembeli)
    print(" Beli :", Gelas, jenis1, "-", total1)
    print(" ", porsi, jenis2, "-", total2)
    print(" Tagihan : Rp.", totalsemua)
    print(" Uang : Rp.", uang)
    print(" Kembalian : Rp.", kembalian)
    print("==========================================")
    print("==========================================")
    ulang()

programkasir()
