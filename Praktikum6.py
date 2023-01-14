# NAMA : Aizan Syalim
# NIM  : 223200231
# STRUKTUR DATA


print("\nPROGRAM 1")
alist = [i for i in range(1,10)]
print ("list angka,", alist)

genap = 0
ganjil = 0

for i in alist:
    if i %2 == 0:
        genap += 1
print("Jumlah bilangan genap: ", genap)
for i in alist:
    if i %2 != 0:
        ganjil += 1
print("Jumlah bilangan ganjil: ", ganjil)

print("\nPROGRAM 2")
bil = int(input("input sebuah angka: "))

for i in range(1,11):
    hasil = bil*i
    print(bil, "x", i, "=", hasil)
    
print("\nPROGRAM 3")
a = 1
b = 1
c = 11
d = 0

while d < c:
    print(a)
    ab = a + b
    a = b
    b = ab 
    d += 1

print("\nPROGRAM 4")
for j in range(1,11):
    for k in range(1,11):
        print(j*k, end="\t")
    print()

