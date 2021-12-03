a=0    
while a==0 :
    nama=(input("Nama : "))
    nim=(input("NIM : "))
    nilaitugas=int(input("Nilai Tugas : "))
    nilaiuts=int(input("Nilai UTS :"))
    nilaiuas=int(input("Nilai UAS :"))
    p1 = input("Tambah Data (y/t)? : ")
    if p1=="t":
        continue
    nama1=(input("Nama : "))
    nim1=(input("NIM : "))
    nilaitugas1=int(input("Nilai Tugas : "))
    nilaiuts1=int(input("Nilai UTS :"))
    nilaiuas1=int(input("Nilai UAS :"))

    p2 = input("Tambah Data (y/t)? : ")
    if p2=="t":
        break
    
d = [
    [1, nama, nim, nilaitugas, nilaiuts, nilaiuas,(nilaitugas*0.3)+(nilaiuts*0.35)+(nilaiuas*0.35) ],
    [2, nama1, nim1, nilaitugas1, nilaiuts1, nilaiuas1,(nilaitugas1*0.3)+(nilaiuts1*0.35)+(nilaiuas1*0.35)]
    ]

print("                                             DATA LIST")
print("="*(26*4))
for baris in range (len(d)):
    for kolom in range (1):
        if baris == 0 and kolom == 0:
            print("||"+"NO".center(12),"||"+"NIM".center(12),
                  "||"+"NAMA".center(12),"||"+"NILAI TUGAS".center(12),
                  "||"+"NILAI UTS".center(12),"||"+"NILAI UAS".center(12),
                  "||"+"NILAI AKHIR".center(12))
            print("="*(26*4))
            
    for kolom in range (7):
        if kolom == 0:
            print("||"+str(d[baris][kolom]).center(12), end=" ")
        else:
            print("||"+str(d[baris][kolom]).center(12), end=" ")
    
    print(" ")
print("="*(26*4)) 
