#71200580

#Soal 1

'''Saat pandemi ini berdampak buruk bagi pendidikan kita semua dari SD,SMP,SMA hingga mahasiswa terkena dampak
oleh karena itu bagi mahasiswa yang melanjutkan studi di Universitas Kristen Duta Wacana yang terkena dampak 
akibat pandemi Covid-19 diberikan kemudahan mengenai biaya dalam pembayaran UKT Semester . mahasiswa yang 
ingin mendapatkan bantuan pembayaran UKT Semester dapat mengisi formulir pendaftaran online yang disiapkan
oleh kampus . jika kamu sebagai seorang mahasiswa informatika di kampus UKDW kamu dapat membantu membuat 
formulir pendaftaran online berupa inputan user untuk mengisi biodata secara lengkap, ditambah dengan
keterangan orang tua, keterangan pekerjaan dan keterangan penghasilan orang tua'''

#masukkan input biodata lengkap untuk formulir pendaftaran online bantuan UKT Semester

Nama = input('Nama Lengkap:')
NIM = input('NIM:')
Tempat = input('Tempat Lahir:')
Tanggal = input('Tanggal Lahir:')
Tahun = input('Tahun Lahir:')
Alamat = input('Alamat Domisili:')
Status = input('Status:')
Jenis_Kelamin = input('Jenis kelamin:')
print('===============================================')
Nama_Ayah = input('Nama Ayah:')
Pekerjaan = input('Pekerjaan:')
Penghasilan = input('Penghasilan:')
print('================================================')
Nama_Ibu = input('Nama Ibu:')
Pekerjaan = input('Pekerjaan:')
Penghasilan = input('Penghasilan:')
print('=================================================')

#Soal 2

'''buatlah program untuk menghitung total pembayaran dari pembelian seorang pelanggan di toko Aukah Gelap
dengan ketentuan pembelian pelanggan sama dengan atau melebihi 200.000,maka pelanggan mendapatkan diskon
sebesar 15%, jika tidak pelanggan hanya mendapatkan discount sebesar 7%'''

Nama_toko = 'Toko Aukah Gelap'
print('~~~~~~~~~~~~~~~~~~~~~~~~~~Toko Aukah Gelap~~~~~~~~~~~~~~~~~~~~~~~~~')
total = 185000
setelah_diskon = total
if total < 200000:
     diskon = total * (7/100)
else:
     diskon = total * (15/100)
setelah_diskon = total - diskon
print('diskonnya yaitu: {} '. format(int(diskon)))
print('harga setelah diskon: {} '. format(int(setelah_diskon)))
print('=========================================================================')