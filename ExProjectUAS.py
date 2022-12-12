def pertama():
    print('\n\t    Selamat Datang di KAI access')  
    print('   Berikut List Rute berdasarkan Class dan Harga')
    no = {"rute" : "Yogyakarta(LPN)\t", "class" : "Eksekutif\t", "harga" : "450.000"}
    n2 = {"rute" : "tujuan\t\t", "class" : "Bisnis\t\t", "harga" : "300.000"}
    n3 = {"rute" : "Surabaya(SGU)\t", "class" : "Ekonomi\t", "harga" : "150.000"}
    n4 = {"rute" : "Jakarta(GMR)\t", "class" : "Ekonomi\t", "harga" : "150.000"}
    print("="*50)
    print("Rute\t\t ","Class\t\t", "Harga\t\t")
    print("="*50)
    print(no["rute"],no["class"],no["harga"])
    print(n2["rute"],n2["class"],n2["harga"])
    print(n3["rute"],n3["class"],n3["harga"])
    print("="*50)
    print("\n")
    print("="*50)
    print("Rute\t\t ","Class\t\t", "Harga\t\t")
    print("="*50)
    print(no["rute"],no["class"],no["harga"])
    print(n2["rute"],n2["class"],n2["harga"])
    print(n4["rute"],n3["class"],n3["harga"])
    print("="*50)

    def welcome() :
        awal=input('\nApakah anda ingin melakukan pemesanan tiket YA/TIDAK : ')
        if awal=='YA' or awal == 'ya':
            print('')
        elif awal=='TIDAK' or awal == 'tidak' :
            pertama()
        else:
            print('Pilihan tidak sesuai!')
            print('Silahakan memilih YA / TIDAK')
            welcome()
    welcome()

    nama =input('Silahkan masukan Nama Anda : ')
    print('Nama :',nama)
    nomor=int(input('Silahkan masukan Nomor Whatsapp Anda : '))
    print('Nomor Whatsapp anda : +62',nomor)

    RuteKereta=['\n1.Yogyakarta(LPN) - Surabaya(SGU)','2.Yogyakarta(LPN) - Jakarta(GMR)\n']
    for menu1 in RuteKereta:
        print(menu1)

    def rute() :
        menuKelas=int(input('Silahkan memasukan angka berdasarkan rute perjalanan: '))
        if menuKelas == 1 :
            print('\nSilahkan Pilih Kereta Pada rute Yogyakarta - Surabaya: ')
            print('1. Pasundan (18.35)')
            print('2. Gaya Baru Malam Selatan (20.10) \n')
            kereta = int(input("Pilih kereta sesuai dengan angka: "))
            if kereta == 1:
                print("Rute Yogyakarta - Surabaya, Kereta Pasundan (18.35)")
            elif kereta == 2:
                print("Rute Yogyakarta - Surabaya, Kereta Gaya Baru Malam Selatan (20.10)")
            else:
                print("Pilihan tidak tersedia")
        elif menuKelas == 2 :
            print('\nSilahkan Pilih Kereta Pada rute Yogyakarta - Jakarta: ')
            print('1. Gajayana (20.14)')
            print('2. Taksaka (21.10) \n')
            kereta = int(input("Pilih kereta sesuai dengan angka: "))
            if kereta == 1:
                print("Rute Yogyakarta - Jakarta, Kereta Gajayana (20.14)")
            elif kereta == 2:
                print("Rute Yogyakarta - Jakarta, Kereta Taksaka (21.10)")
            else:
                print("Pilihan tidak tersedia")
        else:
            print('Pilihan tidak sesuai!')
            rute()
    rute()

    print('\nTiket kereta berdasarkan class')
    menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
    for menu2 in menuPemesanan:
            print(menu2)

    def kelas() :
                menuKelas=int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                if menuKelas == 1:
                    print('\nEksekutif Class')
                    kelas1 = 450000
                    print('Siapkan uang dengan nominal:', kelas1)

                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran=int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            print('\nSilahkan ambil struk kemudian bayar tunai di loket KAI:\n',"Nama\t\t: ",nama ,"\n Nomor Whatsapp\t: ", '+62', nomor)
                            print('Terima kasih telah melakukan pemesanan tiket')
                        elif metodePembayaran == 2:
                            uang=int(input('Silahkan masukan uang sebesar Rp.450000: '))
                            if  uang >= 450000:
                                hasil = uang-450000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,'+62',nomor)
                            elif uang < 450000:
                                print('Mohon maaf, Uang Anda tidak mencukupi')
                                metode()
                            elif uang == 450000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,'+62',nomor)
                        else: 
                            print('Mohon maaf pilihan tidak tersedia')
                            metode()
                    metode()
                if menuKelas == 2:
                    print('\nBisnis Class')
                    kelas2 = 300000
                    print('Siapkan uang dengan nominal:', kelas2)
                    
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran=int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            print('\nSilahkan ambil struk kemudian bayar tunai di loket KAI:\n',"Nama\t\t: ",nama ,"\n Nomor Whatsapp\t: ", '+62', nomor,)
                            print('Terima kasih telah melakukan pemesanan tiket')
                        elif metodePembayaran == 2:
                            uang = int(input('Silahkan masukan uang sebesar Rp.300000: '))
                            if  uang >= 300000:
                                hasil = uang - 300000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,'+62',nomor)
                            elif uang < 300000:
                                print('Mohon maaf, Uang Anda tidak mencukupi')
                                metode()
                            elif uang == 300000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,'+62',nomor)
                        else: 
                            print('Mohon maaf pilihan tidak tersedia')
                            metode()
                    metode()
                elif menuKelas == 3:
                    print('\nEkonomi Class')
                    kelas3 = 150000
                    print('Siapkan uang dengan nominal:', kelas3)

                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            print('\nSilahkan ambil struk kemudian bayar tunai di loket KAI:',"\nNama\t\t: ",nama ,"\n Nomor Whatsapp\t: ", '+62', nomor)
                            print('Terima kasih telah melakukan pemesanan tiket')

                        elif metodePembayaran == 2:
                            uang = int(input('Silahkan masukan uang sebesar Rp.150000: '))
                            if  uang >= 150000:
                                hasil=uang-150000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,'+62',nomor)

                            elif uang < 150000:
                                print('Mohon maaf, Uang Anda tidak mencukupi')
                                metode()
                            elif uang == 150000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,'+62',nomor)
                        else: 
                            print('Mohon maaf pilihan tidak tersedia')
                            metode()
                    metode()
                else:
                    print('Mohon maaf pilihan tidak tersedia')
                    kelas()
    kelas()
    def last():
            again = (input('Apakah anda ingin melakukan pembelian lagi (y/n)'))
            if again == 'y':
                pertama()
            elif again == 'n':
                print('Terima kasih telah melakukan pembelian')
                quit()
            else:
                print('Pilihan tidak sesuai!')
                last()

    last()
pertama()