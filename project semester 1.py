
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
        pilih = input('Masukkan pilihan anda: ')
        if pilih == 1:
            print('harganya mahal yak!!')
        elif pilih == 2:
            print('KAMU MAU BELI JAKET???')
        elif pilih == 3:
            print('KAMU MAU BELI GELANG???')
        elif pilih == 4:
            print('KAMU MAU BELI TOPI???')
        else:
            "ULANGI PILIHAN PRODUK"
            produk()
produk()


    
