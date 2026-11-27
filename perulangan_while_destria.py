suhu=0
while suhu<100:
    print(suhu)
    suhu+=40

if suhu>50:
    print("suhu naik")

for i in range(0,5):
    if i==3:
        print("angka 3 didapat")
        break
    print(i)

for i in range(5):
    if i==3:
        pass
    elif i:=3:
        print("ini selain 3")
    print("angka sekarang: ",i)

for i in range(5):
    if i==3:
        pass #ingin memproses
    elif i:=3:
        print("angka {} bukan 3".format(i))