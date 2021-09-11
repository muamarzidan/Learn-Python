def BubbleSort(val):
    for passnum in range(len(val) - 1, 0, -1):
        for i in range(passnum):
            if val[i] > val[i + 1]:
                temp = val[i]
                val[i] = val[i + 1]
                val[i + 1] = temp


DaftarAngka = [29, 10, 52, 100, 3, 19, 13, 25]
BubbleSort(DaftarAngka)
print(DaftarAngka)