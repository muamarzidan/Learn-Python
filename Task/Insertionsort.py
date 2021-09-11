def InsertionSort(val):
    for index in range(1, len(val)):

        valueaktif = val[index]
        posisi = index

        while posisi > 0 and val[posisi - 1] > valueaktif:
            val[posisi] = val[posisi - 1]
            posisi = posisi - 1

        val[posisi] = valueaktif

DaftarAngka = [32, 6, 48, 54, 3, 18, 12, 24]
InsertionSort(DaftarAngka)
print(DaftarAngka)