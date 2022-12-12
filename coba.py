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
                        elif metodePembayaran== 2:
                            uang=int(input('Silahkan masukan uang sebesar Rp.450000: '))
                            if  uang >= 450000:
                                hasil=uang-450000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,' ',nomor)
                            elif uang < 450000:
                                print('uang anda tidak mencukupi')
                                metode()
                            elif uang == 450000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,' ',nomor)
                        else: 
                            print('Mohon maaf inputan tidak tersedia')
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
                        elif metodePembayaran== 2:
                            uang=int(input('Silahkan masukan uang sebesar Rp.300000: '))
                            if  uang >= 300000:
                                hasil=uang-300000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,' ',nomor)
                            elif uang < 300000:
                                print('uang anda tidak mencukupi')
                                metode()
                            elif uang == 300000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,' ',nomor)
                        else: 
                            print('Mohon maaf inputan tidak tersedia')
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
                        metodePembayaran=int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            print('\nSilahkan ambil struk kemudian bayar tunai di loket KAI:\n',"Nama\t\t: ",nama ,"\n Nomor Whatsapp\t: ", '+62', nomor)
                            print('Terima kasih telah melakukan pemesanan tiket')

                        elif metodePembayaran== 2:
                            uang=int(input('Silahkan masukan uang sebesar Rp.150000: '))
                            if  uang >= 150000:
                                hasil=uang-150000
                                print('Kembalian uang anda',hasil)
                                print('Pembayaran selesai,menampilkan tiket online',nama,'+62',nomor)

                            elif uang < 150000:
                                print('uang anda tidak mencukupi')
                                metode()
                            elif uang == 150000:
                                print('Pembayaran selesai,pemesanan atas nama',nama,'+62',nomor)
                        else: 
                            print('Mohon maaf inputan tidak tersedia')
                            metode()
                    metode()
                else:
                    print('Mohon maaf inputan tidak tersedia')
                    kelas()
    kelas()