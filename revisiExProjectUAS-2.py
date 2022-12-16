def pertama():
    def tabel():
        print('\n\t    Selamat Datang di KAI access')  
        print('   Berikut List Rute berdasarkan Class dan Harga')
        J1 = {"rute" : "|Yogyakarta(LPN)", "class" : " |Eksekutif\t\t", "harga" : "|450.000|"}
        J2 = {"rute" : "|Yogyakarta(LPN)", "class" : " |Eksekutif\t\t", "harga" : "|500.000|"}
        J3 = {"rute" : "|Yogyakarta(LPN)", "class" : " |Eksekutif\t\t", "harga" : "|480.000|"}
        J11 = {"rute" : "|    tujuan\t", "class" : " |Bisnis\t\t", "harga" : "|300.000|"}
        J22 = {"rute" : "|    tujuan\t", "class" : " |Bisnis\t\t", "harga" : "|350.000|"}
        J33 = {"rute" : "|    tujuan\t", "class" : " |Bisnis\t\t", "harga" : "|330.000|"}
        J111 = {"rute" : "|Surabaya(SGU)\t", "class" : " |Ekonomi\t\t", "harga" : "|150.000|"}
        J222 = {"rute" : "|Jakarta(GMR)\t", "class" : " |Ekonomi\t\t", "harga" : "|200.000|"}
        J333 = {"rute" : "|Bandung(PDL)\t", "class" : " |Ekonomi\t\t", "harga" : "|180.000|"}
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print("|Rute\t\t ","|Class\t\t", "|Harga\t |")
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print(J1["rute"],J1["class"],J1["harga"])
        print(J11["rute"],J11["class"],J11["harga"])
        print(J111["rute"],J111["class"],J111["harga"])
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print("\n")
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print("|Rute\t\t ","|Class\t\t", "|Harga\t |")
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print(J2["rute"],J2["class"],J2["harga"])
        print(J22["rute"],J22["class"],J22["harga"])
        print(J222["rute"],J222["class"],J222["harga"])
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print("\n")
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print("|Rute\t\t ","|Class\t\t", "|Harga\t |")
        print("+","="*15,"+","="*20,"+","="*5,"+")
        print(J3["rute"],J3["class"],J3["harga"])
        print(J33["rute"],J33["class"],J33["harga"])
        print(J333["rute"],J333["class"],J333["harga"])
        print("+","="*15,"+","="*20,"+","="*5,"+")
    tabel()

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

    def rincian():
        print("\n")
        print("="*40)
        print("="*5,"STRUK PEMESANAN TIKET KERETA", "="*5)
        print("="*40)
        print("Nama\t\t: ", nama)
        print("Nomor Whatsapp  :  +62", nomor)
        print("Rute \t\t: ", menurute)
        print("Kereta  \t: ", kereta)
        print("Class \t\t: ", pilihclass)
        print("Uang Anda \t: ", uangku)
        print("kembalian \t: ", kembalian)
        print("="*40)
        print('TERIMA KASIH TELAH MELAKUKAN PEMESANAN TIKET')
        print("="*40,'\n')
    
    print('='*40)
    nama =input('Silahkan masukan Nama Anda : ')
    print('NAMA :',nama)
    nomor=int(input('Silahkan masukan Nomor Whatsapp Anda : '))
    print('NOMOR WHATSAPP ANDA : +62',nomor)
    print('='*40)
    
    
    RuteKereta=['1.Yogyakarta(LPN) - Surabaya(SGU)','2.Yogyakarta(LPN) - Jakarta(GMR)','3.Yogyakarta(LPN) - Bandung(PDL)\n']
    print('\nBERIKUT ADALAH RUTE KAI HARI INI')
    for menu1 in RuteKereta:
        print(menu1)

    def rute() :
        global pilihclass
        global menurute
        global kereta
        global harga
        global uangku
        global kembalian
        
        menurute=int(input('Silahkan memasukan angka berdasarkan rute perjalanan: '))
### JOGJA - SURABAYA
        if menurute == 1 :
            menurute = 'Yogyakarta (LPN) - Surabaya (SGU)'
            print('\nPILIHAN KERETA TUJUAN YOGYAKARTA - SURABAYA: ')
            print('1. Pasundan (18.35)')
            print('2. Gaya Baru Malam Selatan (20.10) \n')
            kereta = int(input("Pilih kereta sesuai dengan angka: "))
            if kereta == 1:
                kereta = 'Pasundan (18.35)'
                print("Rute Yogyakarta - Surabaya, Kereta Pasundan (18.35)")
                
                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
                    print('Eksekutif Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                        rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.450000 ')
                        totalsemua = 450000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 450000:
                        print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                        print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                
                    elif uangku == 450000:
                        rincian()
                    else: 
                        print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                        print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                        print('Tunai atau Non-Tunai')
                          
                elif pilihclass == 2:
                    pilihclass = "Bisnis Class"
                 
        
                    print('Bisnis Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.300000 ')
                        totalsemua = 300000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 300000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 300000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                       
                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    
        
                    print('Ekonomi Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.150000 ')
                        totalsemua = 150000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 150000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 150000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                                    
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')
                    metode()

            elif kereta == 2:
                kereta = 'Gaya Baru Malam Selatan (20.10)'
                print("Rute Yogyakarta - Surabaya, Kereta Gaya Baru Malam Selatan (20.10)")

                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
        
                    print('Eksekutif Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.450000 ')
                        totalsemua = 450000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 450000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 450000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                       
                elif pilihclass == 2:
                    pilihclass = "Bisnis Class"
                    
                    print('Bisnis Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            
                        print('\nTotal yang harus dibayar sebesar Rp.300000 ')
                        totalsemua = 300000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 300000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku== 300000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                        

                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    print('Ekonomi Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.150000 ')
                        totalsemua = 150000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 150000:
                        print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                        print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                
                    elif uangku == 150000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                                        
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')
                    metode()

            else:
                print("Pilihan tidak tersedia")
                rute()
### END JOGJA - SURABAYA

### JOGJA - JAKARTA
        elif menurute == 2 :
            menurute = 'Yogyakarta (LPN) - jakarta (GMR)'
            print('\nPILIHAN KERETA TUJUAN YOGYAKARTA - JAKARTA: ')
            print('1. Gajayana (20.14)')
            print('2. Taksaka (21.10) \n')
            kereta = int(input("Pilih kereta sesuai dengan angka: "))
            if kereta == 1:
                kereta = 'Gajayana (20.14)'
                print("Rute Yogyakarta - Jakarta, Kereta Gajayana (20.14)")
                
                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
                    print('Eksekutif Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai') 
                    
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                        print('\nTotal yang harus dibayar sebesar Rp.500000 ')
                        totalsemua = 500000
                        uangku = int(input("Uang : Rp "))
                        kembalian = int(uangku-totalsemua)
                        print("Kembalian : ", kembalian)
                        rincian()
                    elif uangku < 500000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 500000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                          

                elif pilihclass == 2:
                    print('Bisnis Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai') 
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            print('\nTotal yang harus dibayar sebesar Rp.350000 ')
                            totalsemua = 350000
                            uangku = int(input("Uang : Rp "))
                            kembalian = int(uangku-totalsemua)
                            print("Kembalian : ", kembalian)
                            rincian()
                    elif uangku < 350000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 350000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()

                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    print('Ekonomi Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai') 
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            print('\nTotal yang harus dibayar sebesar Rp.200000 ')
                            totalsemua = 200000
                            uangku = int(input("Uang : Rp "))
                            kembalian = int(uangku-totalsemua)
                            print("Kembalian : ", kembalian)
                            rincian()
                    elif uangku < 200000:
                            print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                
                    elif uangku == 200000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()                
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')
                    rute()

            elif kereta == 2:
                kereta = 'Taksaka (21.10)'
                print("Rute Yogyakarta - Jakarta, Kereta Taksaka (21.10)")

                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
                    print('Eksekutif Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')              
                    
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            print('\nTotal yang harus dibayar sebesar Rp.500000 ')
                            totalsemua = 500000
                            uangku = int(input("Uang : Rp "))
                            kembalian = int(uangku-totalsemua)
                            print("Kembalian : ", kembalian)
                            rincian()
                            
                    elif uangku < 500000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 500000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                         
                elif pilihclass == 2:
                    pilihclass = "Bisnis Class"
                    print('Bisnis Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                    
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            print('\nTotal yang harus dibayar sebesar Rp.350000 ')
                            totalsemua = 350000
                            uangku = int(input("Uang : Rp "))
                            kembalian = int(uangku-totalsemua)
                            print("Kembalian : ", kembalian)
                            rincian()
                            
                            
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                         
                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    print('Ekonomi Class')
                                
                    print('1.Tunai')
                    print('2.Non Tunai')
                                  
                   
                    metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                    if metodePembayaran == 1 :
                            rincian()
                    elif metodePembayaran == 2:
                            print('\nTotal yang harus dibayar sebesar Rp.200000')
                            totalsemua = 200000
                            uangku = int(input("Uang : Rp "))
                            kembalian = int(uangku-totalsemua)
                            print("Kembalian : ", kembalian)
                            rincian()
                    elif uangku < 200000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                    elif uangku == 200000:
                                rincian()
                    else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                                      
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')
                    rute()

            else:
                print("Pilihan tidak tersedia")
                rute()
### END JOGJA - JAKARTA

### JOGJA - BANDUNG
        elif menurute == 3 :
            menurute = 'Yogyakarta (LPN) - Bandung(PDL)'
            print('\nPILIHAN KERETA TUJUAN YOGYAKARTA - BANDUNG: ')
            print('1. Mutiara Selatan Priority (22.05)')
            print('2. Saring (20.45) \n')
            kereta = int(input("Pilih kereta sesuai dengan angka: "))
            if kereta == 1:
                kereta = 'Mutiara Selatan Priority (22.05)'
                print("Rute Yogyakarta - Bandung, Mutiara Selatan Priority (22.05)")
                
                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
                    harga = 480000
                    print('\nEksekutif Class')
                    print('Siapkan uang dengan nominal : Rp.480000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.480000: '))
                            if  uang > 480000:
                                hasil = uang - 480000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 480000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 480000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()

                elif pilihclass == 2:
                    pilihclass = "Bisnis Class"
                    harga = 330000
                    print('\Bisnis Class')
                    print('Siapkan uang dengan nominal : Rp.330000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.330000: '))
                            if  uang > 330000:
                                hasil = uang - 330000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 330000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 330000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()

                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    harga = 180000
                    print('\Ekonomi Class')
                    print('Siapkan uang dengan nominal : Rp.180000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.180000: '))
                            if  uang > 180000:
                                hasil = uang - 180000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 180000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 180000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()                
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')

            elif kereta == 2:
                kereta = 'Saring (20.45)'
                print("Rute Yogyakarta - Bandung, Saring (20.45))")
                print('\nTiket kereta berdasarkan class')
                menuPemesanan = ['1. Eksekutif','2. Bisnis','3. Ekonomi']
                for menu2 in menuPemesanan:
                    print(menu2)
                pilihclass = int(input('Masukan angka berdasarkan angka kelas yg tersedia: '))
                
                if pilihclass == 1:
                    pilihclass = "Eksekutif Class"
                    harga = 480000
                    print('\nEksekutif Class')
                    print('Siapkan uang dengan nominal : Rp.480000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.480000: '))
                            if  uang > 480000:
                                hasil = uang - 480000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 480000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 480000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()

                elif pilihclass == 2:
                    pilihclass = "Bisnis Class"
                    harga = 330000
                    print('\Bisnis Class')
                    print('Siapkan uang dengan nominal : Rp.330000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.330000: '))
                            if  uang > 330000:
                                hasil = uang - 330000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 330000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 330000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()

                elif pilihclass == 3:
                    pilihclass = "Ekonomi Class"
                    harga = 180000
                    print('\Ekonomi Class')
                    print('Siapkan uang dengan nominal : Rp.180000')
                    print('\nMetode Pembayaran tiket')                
                    metodepembayaran = ['1.Tunai', '2.Non Tunai']
                    for menu3 in metodepembayaran:
                        print(menu3)
                    def metode():
                        metodePembayaran = int(input('Masukan angka berdasarkan metode pembayaran: '))
                        if metodePembayaran == 1 :
                            rincian()
                        elif metodePembayaran == 2:
                            uang=int(input('\nSilahkan masukan uang sebesar Rp.180000: '))
                            if  uang > 180000:
                                hasil = uang - 180000
                                print('Kembalian uang anda',hasil)
                                rincian()
                            elif uang < 180000:
                                print('MOHON MAAF, UANG ANDA TIDAK MENCUKUPI')
                                print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN!!\n')
                                metode()
                            elif uang == 180000:
                                rincian()
                        else: 
                            print('\nMOHON MAAF, PILIHAN TIDAK TERSEDIA')
                            print('SILAHKAN ULANGI LAGI METODE PEMBAYARAN\n')
                            print('Tunai atau Non-Tunai')
                            metode()
                    metode()                
                else:
                    print('MOHON MAAF INPUTAN TIDAK TERSEDIA')

            else:
                print("Pilihan tidak tersedia")
                rute()
### END JOGJA - BANDUNG
        else:
            print('Pilihan tidak sesuai!')
            rute()
    rute()

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