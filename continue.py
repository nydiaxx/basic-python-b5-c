for i in range(5):
    if i == 3:
        continue
    # program dibawah ini tidak akan dieksekusi,
    # ketika continue aktif
    print(i)

for i in range(5):
    q = input("Masukkan kode : ")
    if q == 'n':
        print("Angka diskip")
        continue
    # program dibawah ini tidak akan dieksekusi,
    # ketika continue aktif
    print(i)