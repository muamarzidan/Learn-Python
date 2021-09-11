#positifnegatif    #ganjilgenap
print("\nMenentukan bilangan ganjilgenap positifnegatif")
input_bilangan = input("Masukan bilangan : ")
bilangan = int(input_bilangan)
if (bilangan<0)  and (bilangan % 2 ==0):
    print(bilangan, "Merupakan bilangan genap negatif")

elif (bilangan<0) and (bilangan % 2 ==1):
    print(bilangan, "Merupakan bilangan ganjil negatif")

elif (bilangan>0)  and (bilangan % 2 ==1):
    print(bilangan, "Merupakan bilangan ganjil positif")

elif (bilangan>0) and (bilangan % 2 ==0):
    print(bilangan, "Merupakan bilangan genap positif")

else:
    print(bilangan, "Merupakan bilangan istimewa")
