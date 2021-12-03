print("="*45)
print("Membuat 5 element")
a = [2,4,6,8,10]
print(a)
print("="*45)
print("Menampilkan elemen ke3")
a  = [2,4,6,8,10]
print(a[2])
print("="*45)
print("Mengambil elemen ke 2 sampai ke 4")
a  = [2,4,6,8,10]
print(a[1:4])
print("="*45)
print("Mengambil elemen terakhir")
a  = [2,4,6,8,10]
print(a[4])
print("="*45)
print("Mengubah elemen ke4")
a  = [2,4,6,8,10]
a[3]=9
print(a)
print("="*45)
print("Mengubah elemen ke 4  sampai terakhir")
a  = [2,4,6,8,10]
a[3:5]=16,20
print(a)
print("="*45)
print("Mengambil 2 bagian dari list a menjadi list b")
a = [2,4,6,8,10]
b = [2,4]
print(a,b)
print("="*45)
print("Menambahkan list b dengan nilai string")
a = [2,4,6,8,10]
b = [2,4]
b.append(5)
print(b)
print("="*45)
print("Menambahkan list b dengan 3 nilai")
a = [2,4,6,8,10]
b = [2,4]
b.extend([200,300,400])
print(b)
print("="*45)

print("Menggabungkan list b dengan a")
a = [2,4,6,8,10]
b = [2,4]
c = b + a
print(c)
print("="*45)
