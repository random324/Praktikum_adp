n=int(input("masikkan jumlah pendaftar :"))
for i in range (1,n+1):
    print(f"{i} ----------------------------------------------------------------------------------->")
    nama=input("nama :")
    matkul=input("matkul :")
    a=0
    while a<=0:
        wawancara=int(input("Masukkan nilai wawancara :"))
        if wawancara >= 0 and wawancara<=100:
            a+=1
        else:
             print("angka yang anda masukkan tidak termasuk ke dalam rentang nilai")
        continue
    b=0
    while b<=0:
        tulis=int(input("Masukkan nilai tulus :"))
        if tulis >= 0 and tulis <=100:
            b+=1
        else:
             print("angka yang anda masukkan tidak termasuk ke dalam rentang nilai")
        continue
    c=0
    while c<=0:
        mengajar=int(input("Masukkan nilai mengajar :"))
        if mengajar >= 0 and mengajar<=100:
            c+=1
        else:
             print("angka yang anda masukkan tidak termasuk ke dalam rentang nilai")
        continue
    rata_rata=(wawancara+tulis+mengajar)/3
    yes="LULUS"
    no="TIDAK LULUS"
    if rata_rata >= 80:
        print(f"Nama :{nama}|Mata Kuliah :{matkul}|Rata-Rata :{"%.1f" %(rata_rata)}|Prediket :{yes}")
    else:
        print(f"Nama :{nama}|Mata Kuliah :{matkul}|Rata-Rata :{"%.1f" %(rata_rata)}|Prediket :{no}")