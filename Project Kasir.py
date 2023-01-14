print("===========TOKO CAKMAN===========")
Pembeli = input("Nama Pembeli : ")
print('Nama Pembeli : ', Pembeli)

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===========MENU MAKANAN 1===========")
    print("1. Nasi Kuning - Rp.4000,00")
    print("2. Nasi Goreng - Rp.5000,00")
    print("3. Nasi Liwet - Rp.10000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    porsi = int(input("Berapa Porsi :"))

    if nomor == 1:
        totalmakanan = porsi * 5000
        print(porsi,' Nasi Kuning = Rp.',totalmakanan)
        makan=("Nasi Kuning")
    elif nomor == 2:
        totalmakanan = porsi * 8000
        print(porsi,' Nasi Goreng = Rp.',totalmakanan)
        makan=("Nasi Goreng")
    elif nomor == 3:
        totalmakanan = porsi * 10000
        print(porsi,' Nasi Liwet = Rp.',totalmakanan)
        makan=("Nasi Liwet")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        makanan()

def makanan2():
    global totalmakanan2
    global porsi2
    global makan2
    print("\n===========MENU MAKANAN 2===========")
    print("1. Nasi Kuning - Rp.5000,00")
    print("2. Nasi Goreng - Rp.8000,00")
    print("3. Nasi Liwet - Rp.10000,00")
    print("4. Skip")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    porsi2 = int(input("Berapa Porsi :"))

    if nomor == 1:
        totalmakanan2 = porsi2 * 5000
        print(porsi2,' Nasi Kuning = Rp.',totalmakanan2)
        makan2=("Nasi Kuning")
    elif nomor == 2:
        totalmakanan2 = porsi2 * 8000
        print(porsi2,' Nasi Goreng = Rp.',totalmakanan2)
        makan2=("Nasi Goreng")
    elif nomor == 3:
        totalmakanan2 = porsi2 * 10000
        print(porsi2,' Nasi Liwet = Rp.',totalmakanan2)
        makan2=("Nasi Liwet")
    elif nomor == 4:
        totalmakanan2 = porsi2 * 0
        print(porsi2, "Skip", totalmakanan)
        makan2=(" ")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        makanan2()()

def makanan3():
    global totalmakanan3
    global porsi3
    global makan3
    print("\n===========MENU MAKANAN 3===========")
    print("1. Nasi Kuning - Rp.5000,00")
    print("2. Nasi Goreng - Rp.8000,00")
    print("3. Nasi Liwet - Rp.10000,00")
    print("4. Skip")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    porsi3 = int(input("Berapa Porsi :"))

    if nomor == 1:
        totalmakanan3 = porsi3 * 5000
        print(porsi3,' Nasi Kuning = Rp.',totalmakanan3)
        makan3=("Nasi Kuning")
    elif nomor == 2:
        totalmakanan3 = porsi3 * 8000
        print(porsi3,' Nasi Goreng = Rp.',totalmakanan3)
        makan3=("Nasi Goreng")
    elif nomor == 3:
        totalmakanan3 = porsi3 * 10000
        print(porsi3,' Nasi Liwet = Rp.',totalmakanan3)
        makan3=("Nasi Liwet")
    elif nomor == 4:
        totalmakanan3 = porsi3 * 0
        print(porsi3, "Skip", totalmakanan3)
        makan3=(" ")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        makanan3()()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===========MENU MINUMAN 1===========")
    print("1. Es Dawet - Rp.3000,00")
    print("2. Es Timun Suri - Rp.4000,00")
    print("3. Es Oyen - Rp.6000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    gelas = int(input("Berapa Gelas :"))

    if nomor == 1:
        totalminuman = gelas * 3000
        print(gelas,' Es Dawet = Rp.',totalminuman)
        minum=("Es Dawet")
    elif nomor == 2:
        totalminuman = gelas * 4000
        print(gelas,' Es Timun Suri = Rp.',totalminuman)
        minum=("Es Timun Suri")
    elif nomor == 3:
        totalminuman = gelas * 6000
        print(gelas,' Es Oyen = Rp.',totalminuman)
        minum=("Es Oyen")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        minuman()

def minuman2():
    global totalminuman2
    global gelas2
    global minum2
    print("\n===========MENU MINUMAN 2===========")
    print("1. Es Dawet - Rp.3000,00")
    print("2. Es Timun Suri - Rp.4000,00")
    print("3. Es Oyen - Rp.6000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    gelas2 = int(input("Berapa Gelas :"))

    if nomor == 1:
        totalminuman2 = gelas2 * 3000
        print(gelas2,' Es Dawet = Rp.',totalminuman2)
        minum2=("Es Dawet")
    elif nomor == 2:
        totalminuman2 = gelas2 * 4000
        print(gelas2,' Es Timun Suri = Rp.',totalminuman2)
        minum2=("Es Timun Suri")
    elif nomor == 3:
        totalminuman = gelas2 * 6000
        print(gelas2,' Es Oyen = Rp.',totalminuman2)
        minum2=("Es Oyen")
    elif nomor == 4:
        totalminuman2 = gelas2 * 0
        print(gelas2, "Skip", totalminuman2)
        minum2=(" ")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        minuman2()

def minuman3():
    global totalminuman3
    global gelas3
    global minum3
    print("\n===========MENU MINUMAN 3===========")
    print("1. Es Dawet - Rp.3000,00")
    print("2. Es Timun Suri - Rp.4000,00")
    print("3. Es Oyen - Rp.6000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    gelas3 = int(input("Berapa Gelas :"))

    if nomor == 1:
        totalminuman3 = gelas3 * 3000
        print(gelas3,' Es Dawet = Rp.',totalminuman3)
        minum3=("Es Dawet")
    elif nomor == 2:
        totalminuman3 = gelas3 * 4000
        print(gelas3,' Es Timun Suri = Rp.',totalminuman3)
        minum3=("Es Timun Suri")
    elif nomor == 3:
        totalminuman3 = gelas3 * 6000
        print(gelas3,' Es Oyen = Rp.',totalminuman3)
        minum3=("Es Oyen")
    elif nomor == 4:
        totalminuman3 = gelas3 * 0
        print(gelas3, "Skip", totalminuman3)
        minum3=(" ")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        minuman3()

makanan()
makanan2()
makanan3()
minuman()
minuman2()
minuman3()
total_semua = totalmakanan + totalmakanan2 + totalmakanan3 + totalminuman + totalminuman2 + totalminuman3

print("\nTotal yang harus di bayar : ",total_semua)
uang = int(input("Uang tunai pembeli : Rp."))
kembalian = int(uang - total_semua)
print("kembalian :", kembalian)


print("\n===========S T R U K B E L I===========")
print("Nama\t\t\t:",Pembeli)
print("Makanan 1\t\t:",porsi,makan, "(Rp.", totalmakanan,")")
print("Makanan 2\t\t:",porsi2,makan2, "(Rp.", totalmakanan2,")")
print("Makanan 3\t\t:",porsi3,makan3, "(Rp.", totalmakanan3,")")
print("Minuman\t\t\t:",gelas,minum, "(Rp.", totalminuman,")")
print("Minuman 2\t\t:",gelas2,minum2, "(Rp.", totalminuman2,")")
print("Minuman 3\t\t:",gelas3,minum3, "(Rp.", totalminuman3,")")
print("Tagihan\t\t\t: Rp.",total_semua) 
print("Dibayar\t\t\t: Rp.",uang)
print("Kembalian\t\t: Rp.",kembalian)


print("========================================")