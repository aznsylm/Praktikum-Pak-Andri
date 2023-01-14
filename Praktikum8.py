#PROGRAM PERTAMA

# c = int(input("Masukkan berapa banyak data yang akan diinput : "))
# dict = {}

# for i in range (c):
#     a = int(input("masukkan data key : "))
#     b = input("masukkan data : ")

#     dict[a] = b
# print(dict)

# PROGRAM KEDUA
no= {"KEY" : "\t", "nim" : "223200256\t", "Nama" : "Muhammad Lukman", "SKS" : "100\t" , "Beasiswa" : "1\t\t", "Lahir" : "19/05/04"}
n2= {"KEY" : "MAH001\t", "nim" : "223200257\t", "Nama" : "Muhammad Nopal", "SKS" : "150\t" , "Beasiswa" : "1\t\t", "Lahir" : "01/01/02"}
n3= {"KEY" : "\t", "nim" : "223200258\t", "Nama" : "Andrian Slebew", "SKS" : "100\t" , "Beasiswa" : "0\t\t", "Lahir" : "10/10/10"}
print("="*74)
print("KEY\t","nim\t\t", "Nama\t\t", "SKS\t", "Beasiswa\t", "Lahir")
print("="*74)
print(no["KEY"],no["nim"],no["Nama"],no["SKS"],no["Beasiswa"],no["Lahir"])
print(n2["KEY"],n2["nim"],n2["Nama"],n2["SKS"],n2["Beasiswa"],n2["Lahir"])
print(n3["KEY"],n3["nim"],n3["Nama"],n3["SKS"],n3["Beasiswa"],n3["Lahir"])

no= {"KEY" : "\t", "nim" : "223200256\t", "Nama" : "Muhammad Lukman", "SKS" : "100\t" , "Beasiswa" : "1\t\t", "Lahir" : "19/05/04"}
n2= {"KEY" : "MAH001\t", "nim" : "223200257\t", "Nama" : "Muhammad Nopal", "SKS" : "150\t" , "Beasiswa" : "1\t\t", "Lahir" : "01/01/02"}
n3= {"KEY" : "\t", "nim" : "223200258\t", "Nama" : "Andrian Slebew", "SKS" : "100\t" , "Beasiswa" : "0\t\t", "Lahir" : "10/10/10"}
print("="*50)
print("KEY\t","nim\t\t", "Nama\t\t")
print("="*50)
print(no["KEY"],no["nim"],no["Nama"])
print(n2["KEY"],n2["nim"],n2["Nama"])
print(n3["KEY"],n3["nim"],n3["Nama"])