##########################################
# MENDEFINISAKAN FUNGSI
# zan = str(input("masukkan nama = "))

# def hai_mahasiswa():
#     print(zan)

# hai_mahasiswa()
# hai_mahasiswa()
# hai_mahasiswa()

###########################################
# VARIABEL DALAM FUNCTION
# def cariLuasSegitiga():
#     alas = int(input("Masukkan angka = "))
#     tinggi = int(input("Masukkan angka = ")) 
#     luas = (alas * tinggi) / 2 
#     print("luas segitiganya adalah = ", luas)

# cariLuasSegitiga()
# cariLuasSegitiga()
# cariLuasSegitiga()

###########################################
#CONTOH MEMBUAT FUNGSI PEMANGKATAN
# angka = int(input("masukkan angka : "))
# pangkat = int(input("masukkan pangkat : "))

# def hitung_pangkat(angka, pangkat):
#     if pangkat > 1:
#         return angka * hitung_pangkat(angka, pangkat - 1)

#     return angka

# hasil = hitung_pangkat(angka, pangkat)
# print(f"hasil = {hasil}")


###########################################
# MENENTUKAN GANJIL GENAP
# nilai = int(input("Masukkan angka = "))

# def tentukanGanjilGenap():
#     if nilai % 2 != 0:
#         print(nilai, " adalah bilangan Ganjil")
#     else:
#         print(nilai, " adalah bilangan Genap")

# tentukanGanjilGenap()
# tentukanGanjilGenap()
# tentukanGanjilGenap()

###########################################

# Kode program parameter dan argumen fungsi


###########################################
# perhitungan rata rata
# list [2,3,6,7,9,10]
# def rataRata(p, q, r):
#     return(p + q + r) / 3

# rataRata(3, 4, 5)     

###########################################
# n = int(input("Masukkan nilai n = ")) #misal n nya = 3
# faktorial = 5

# for i in range(1, n + 1):
#     faktorial *= i

# print(f'{n} = {faktorial}')