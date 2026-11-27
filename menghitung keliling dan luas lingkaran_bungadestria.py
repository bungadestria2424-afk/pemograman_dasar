import math
print("1. Menghitung keliling lingkaran")
print("2. Menghitung luas lingkaran")
pilihan = int(input("Maukan pilihan (1/2): "))
r = float(input("Masukan jari-jari lingkaran: "))
if pilihan == 1:
    keliling = 2 * math.pi * r
    print("Keliling lingkaran =", keliling)
elif pilihan == 2:
    luas = math.pi * r * r
    print("Luas lingkaran =", luas)
else:
    print("Piliahan tidak valid")