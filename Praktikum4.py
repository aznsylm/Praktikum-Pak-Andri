# #    KAMIS, 24 Nov 2002
# #    Materi LIST (type data)

# # 1 Akses nilai dalam list python

# # 2 Update nilai dalam list pythoon

# # list = ['sistem', 'teknik', 2008, 2020]
# # print(list)

# # list[2]= 2001
# # print(list)

# # 3 Hapus nilai dalam list python

# # 4 Operasi dasar list python

# print("-"*80)
# list = [1, -2, -8, 0, 3]
# print("Bilangan maksimum adalah ", max(list))

# print("-"*80)
# list = [1, -2, -8, 0, 3]
# print("Bilangan minimum adalah ", min(list))

# # program memfilter string yang terdiri lebih dari 4 huruf
# print("-"*80)
# list1 = ["Pada", "hari", "minggu", "Budi", "dan", "Ani", "belajar", "di", "rumah", "Adi", "di", "Desa", "Konohagakure", "kecamatan", "sukamaju"]
# print("String asli : ", str(list1))

# tes = filter(lambda e: len(e) > 4, list1)
# print("Berikut adalah kata yang lebih dari 4 huruf : ", list(tes) )

# # 
# print("-"*80)
# list = ["Rusa", "Buaya", "Kucing", "Elang", "Bebek"]
# print("Ini adalah listnya : ", list)

# n = 0
# for i in range (len(list)):
#     list.insert(n,"a")
#     n += 2 

# print("Menambahkan 'a' pada setiap kata : ", list)
