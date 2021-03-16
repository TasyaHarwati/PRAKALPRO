#Tasya Setyo Harwati

'''Sebagai seorang Mahasiswa Teknik Informatika anda diminta untuk membuat
suatu deret dengan meminta user untuk inputkan x=5. tampilan harus sesuai
seperti ini.1  
            2  
            3  
            4  
            5  
            1  
            2  
            3  
            4  
            5  
            1  
            2  
            3  
            4  
            5  
            5  
            4  
            3  
            2  
            1  '''

x= int(input("Masukkan x = "))
for i in range(1,x+1):
    if i%2==1:
        for j in range(1,x+1):
           print(j," ",end='\n')
else:
    for j in range(x,0,-1):
        print(j," ",end='\n')
print()

'''sebagai seorang mahasiswa teknik informatika anda diminta untuk membuat
program dengan menampilkan seperti ini
*******
*******
*******
*******
*******
*******
*******
*******. dengan menginputkan jumlah baris = 8 saat membuat program. Tetapi saat
di run harus langsung tertampil bentuk seperti diatas tanpa menyuruh user
untuk menginputkan jumlah baris lagi'''

for i in range(8):
    for j in range(8-1):
        print('*',end="")
    print()
