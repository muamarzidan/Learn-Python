#Belajar if dengan logika OR
print("\nBelajar Logika OR pada Percabangan")
print("Membuat Predikat Nilai")
input_nilai = input("Masukkan Predikat Nilai Anda : ")
if (input_nilai=="A") or (input_nilai=="a") :
    print("Predikat Anda"  , input_nilai, " Nilai Anda Sangat Baik : ")
elif (input_nilai=="B") or (input_nilai=="b") :
    print ("Predikat Anda" , input_nilai, ", Nilai Anda Baik : ")
elif (input_nilai=="C") or (input_nilai=="c") :
    print("Predikat Anda" , input_nilai, ", Nilai Anda Cukup : ")
elif (input_nilai =="D") or (input_nilai == "d") :
    print("Predikat Anda" , input_nilai, ", Nilai Anda Kurang : ")
elif (input_nilai == "E") or (input_nilai == "e") :
    print("Predikat Anda" , input_nilai, ", Nilai Anda Sangat Kurang")
else :
    print("Maaf kode tidak terdefinisi")