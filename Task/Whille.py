print("PENGGUNAAN WHILE")

print("Counter Penambahan")
count = 1
while (count <=10):
    print(count)
    count = count +1

print("Counter Pengurangan")
count = 12
while (count >=1):
    print(count)
    count = count -1


print ("Counter bilangan genap:  ")
count = 23
while(count >=1):
    count = count-1
    if (count%2==0):
        print('%d bilangan genap'%count)
    else:
        continue


print("Counter Bilangan ganjil")
count = 1
while(count <18):
    count = count +1
    if (count%2==1):
        print('%d bilangan ganjil'%count)
    else:
        continue
