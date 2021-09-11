#menentukan bilangan positif atau negatif
print("\nMenentukan bilangan positif atau negatif")
input_bilangan = input("Masukkan sebuah bilangan : ")
bilangan =int(input_bilangan)
if (bilangan <0) :
    print(bilangan, "Merupakan Bilangan Negatif")
elif (bilangan >0) :
    print(bilangan, "Merupakan Bilangan Positif")
else :
    print(bilangan, "Merupakan Bilangan Istimewa")
