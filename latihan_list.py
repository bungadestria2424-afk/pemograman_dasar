penumpang = ["William", "Kate", "Anderson", "jame", "Mady"]
print("a. data awal:", penumpang)

penumpang.append("jones")
print("b. setelah jones masuk:", penumpang)

penumpang[2] = "grace"
print("c. setelah anderson diganti grace:", penumpang)

cek_thompson = "thompson" in penumpang
print("d. apakah ada penumpang bernama thompson?:", cek_thompson)

penumpang.sort()
print("e. urutan tempat duduk sesuai abjad:", penumpang)

print("f. daftar penumpang yang sampai di Yogyakarta:")
for orang in penumpang:
    print("-", orang)

penumpang.clear()
print("g. isi list setelah semua turun:", penumpang)
