
def garis() :
    print('\n')
    print('>'*20,'SELALU STOCK','<'*20)
    print("Jl.Nin dulu aja No.1 tp tidak satu-satunya".center(55))
    print("Kec.Loro Kab.Cidro Prov.Ho'o".center(50))
    print('='*54)
garis()

print("DISKON 10% DENGAN MINIMAL 100K PEMBELIAN".center(55))
print("SILAHKAN AJAK TEMAN KERABAT BERBELANJA".center(55))
print('='*54)
print('BERIKUT ADALAH DAFTAR PRODUK')
listProduk = ['1.KAOS/50k', '2.JAKET/120k', '3.GELANG/10k', '4.TOPI/30k']   
for menu1 in listProduk:
        print(menu1)
def produk():        
        pilih = int(input('Masukkan pilihan anda: '))
        if pilih == 1:    
            print('KAOS (50k/pcs)')
            jumlahBaju = int(input("BERAPA BANYAK KAOS: "))
            produk() 
        elif pilih == 2:
            print('JAKET (120k/pcs)')
            jumlahJaket = int(input("BERAPA BANYAK JAKET: "))
        elif pilih == 3:
            print('GELANG (10k/pcs)')
            jumlahGelang = int(input("BERAPA BANYAK GELANG: "))
        elif pilih == 4:
            print('KAMU MAU BELI TOPI???')
            jumlahTopi = int(input("BERAPA BANYAK TOPI: "))
        else:
            print("ULANGI PILIHAN PRODUK\n")
            produk()
produk()


    
