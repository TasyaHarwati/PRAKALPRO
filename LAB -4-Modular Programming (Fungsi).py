#Tasya Setyo Harwati
#71200580

#Soal 1

'''Sebagai mahasiswa prodi teknik informatika kamu disuruh membuat suatu program untuk menyapa seseorang
dengan fungsi def tanpa return'''

def Menyapa(nama):
    print("Hi, " + nama + ". Bagaimana kabarmu?\t\t\t\t\t\t\t\t\t\t")
Menyapa('Mrs. Torfun\t\t\t\t\t\t\t\t\t')

#Soal 2

'''pada Toko Maju Kanan Maju Kiri sedang mengalami kesulitan dalam menghitung
total harga dan uang kembalian. oleh karena itu sebagai mahasiswa prodi teknik
informatika, kamu diminta membantu membuat suatu program dengan fungsi untuk
menghitung total pembayaran. menggunakan fungsi def total dengan parameter
harga,jumlah.Kamu juga disuruh menambahkan total diskon 15% jika pembeli
membeli baju lebih Rp 120.000 setelah itu jangan lupa untuk
meminta user untuk input harga barang, jumlah baju yang dibeli dan jumlah
nominal uang. Menggunakan fungsi Mengembalikan nilai'''

print("===============Toko Maju Kanan Maju Kiri================")
harga= int(input("masukan harga barang: ")) 
jumlah= int(input("masukan jumlah baju yang dibeli: "))
def total(harga,jumlah):
    return harga*jumlah 
Total=total(harga,jumlah)
if Total>120000:
    Total=Total-(15/100)*Total
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)
