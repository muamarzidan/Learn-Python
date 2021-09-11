def SelectionSort(val):
    for isi in range(len(val) - 1, 0, -1):
        Max = 0
        for lokasi in range(1, isi + 1):
            if val[lokasi] > val[Max]:
                Max = lokasi

        temp = val[isi]
        val[isi] = val[Max]
        val[Max] = temp


DaftarAngka = [30, 5, 45, 75, 15, 25, 50, 60]
SelectionSort(DaftarAngka)
print(DaftarAngka)