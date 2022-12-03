def pertama():
    print("="*50)
    print('Selamat Datang di KAI access')
    print("="*50)

    def welcome() :
        awal=input('Apakah anda ingin melakukan pemesanan tiket YA/TIDAK : ')
        if awal=='YA' or awal == 'ya':
            print('\nSelamat Datang di Menu Pesan Kereta')
        elif awal=='TIDAK' or awal == 'tidak' :
            quit()
        else:
            print('Pilihan tidak sesuai!')
            welcome()
    welcome()

    nama =input('Silahkan masukan nama anda : ')
    print('Nama :',nama)
    nomor=int(input('Silahkan masukan nomor Whatsapp anda : '))
    print('Nomor Whatsapp anda : +62',nomor)

    print('\nRute KAI Hari ini: ')
    RuteKereta=['1.Yogyakarta(LPN) - Surabaya(SGU)','2.Yogyakarta(LPN) - Jakarta(GMR)\n']
    for menu1 in RuteKereta:
        print(menu1, end= '\n')

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
            print('input salah')
            rute()
    rute()
    print('\nTiket kereta brdasarkan class')
    menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi\n']
    for menu2 in menuPemesanan:
        print(menu2, end=' \n')

    def kelas() :
            menuKelas=int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
            if menuKelas== 1:
                print('Selamat datang di VIP Class')
            elif menuKelas == 2:
                 print('Selamat datang di bisnis Class')
            elif menuKelas == 3:
                 print('Selamat datang di ekonmi Class')
            else:
                print('input salah')
                kelas()
    kelas()

    print('Metode Pembayaran tiket')
    metodepembayaran = ['1.Tunai', '2.Non Tunai \n']
    for menu3 in metodepembayaran:
            print(menu3, end='  \n')

    def metode():
        metodePembayaran=int(input('Masukan angka berdasarkan metode pembayaran: '))
        if metodePembayaran== 1 :
            print('Ambil sruk,bayar di loket kereta safiq',nama , ' ', nomor)
            print('Terima kasih telah melakukan tiket')
            exit()
        elif metodePembayaran== 2:
            print('silahkan menyelesaikan')
        else: 
            print('input salaha')
            metode()

        uang=int(input('Silahkan msukan uang sebesar Rp 300000: '))
        if uang>=300000:
            hasil=uang-300000
            print('Kembalian uang anda',hasil)
            print('Pembayaran selesai,menampilkan tiket online',nama,' ',nomor)
        elif uang< 300000:
            print('uang anda tidak mencukupi')
            metode()
    metode()
    def last():
        again=(input('Apakah anda ingin melakukan pembelian lagi (y/n)'))
        if again== 'y':
            pertama()
        elif again=='n':
            print('Terima kasih telah melakukan pembelian')
            quit()
        else:
            print('input salah')
            last()
                
    last()
pertama()
