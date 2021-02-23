#Tasya Setyo Harwati
#71200580

#Soal 1
'''Anda seorang mahasiswa UKDW di Fakultas Teknologi Informasi.Sebagai mahasiswa
Teknik Informatika anda diminta oleh pihak kampus untuk membuat program. Dalam
program tersebut anda meminta user untuk memberikan namanya dan jenis kelaminnya
(laki-laki,perempuan). Jika memilih laki-laki, cetak tulisan Mr dengan diikuti
nama user dan jika memilih perempuan, cetak tulisan Mrs dengan diikuti nama user
'''
Nama = input('Masukkan Nama anda: ')
Gender = input('Laki-laki/Perempuan?: ')
if Gender == 'Laki-laki':
    print('Selamat datang Mr', Nama)
else:
    print('Selamat datang Mrs', Nama)

print('============================================================================')

#Soal 2
'''Anda adalah seorang mahasiswa UKDW. Sebagai mahasiswa Teknik Informatika anda ingin
membuat suatu program yang menyuruh user untuk memasukkan hari yang sesuai perintah anda,
yaitu hari Minggu saat sedang membuat program.jika sudah memasukkan variabel huruf berupa
hari minggu maka, Bagaimana outputnya ?'''

Hari_ini = "Minggu"
if(Hari_ini == 'Senin'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Selasa'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Rabu'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Kamis'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Jumat'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Sabtu'):
    print('Saya akan kuliah')
elif(Hari_ini == 'Minggu'):
    print('FREEDOM')

print('=============================================================================')

#Soal 3
'''Anda adalah seorang mahasiswa UKDW. Sebagai mahasiswa Teknik Informatika anda
ingin membuat suatu program dimana menampilkan teks dari sebuah angka nilai. Variabel asal
yang digunakan berisi angka antara ‘0’ – ‘100’. Kemudian kode program akan
menampilkan hasil tampilan yang berbeda-beda untuk setiap angka,termasuk jika huruf
tersebut di luar '0' - '100'.'''

nilai = int(input("Masukkan nilai anda: "))
if nilai >= 90:
  print('Pertahankan')
elif nilai >= 80 and nilai < 90:
  print('Harus lebih baik lagi')
elif nilai >= 60 and nilai < 80:
  print('Perbanyak belajar')
elif nilai >= 40 and nilai < 60:
  print('Jangan keseringan main')
elif nilai < 40:
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')

print('===============================================================================')
