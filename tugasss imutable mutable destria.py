hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

hari_kedua.add("keju")

barang_sama = hari_pertama.intersection(hari_kedua)
print("c. barang yang sama:", barang_sama)

beli_hari_1_saja = hari_pertama.difference(hari_kedua)
print("d. hanya di hari pertama:", beli_hari_1_saja)

hari_pertama.remove("garam")

beli_hari_2_saja = hari_kedua.difference(hari_pertama)
print("f. hanya di hari kedua:", beli_hari_2_saja)

barang_tidak_sama = hari_pertama.symmetric_difference(hari_kedua)
print("g. baranng tidak sama:", barang_tidak_sama)

print("h. pembelian hari pertama:", hari_pertama)
print("i. pembelian hari kedua:", hari_kedua)


