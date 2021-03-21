#Tasya Setyo Harwatii

#soal 1
'''kamu sebagai mahasiswa teknik informatika diminta bantuan
oleh temanmu untuk membuat program yang dapat menghitung huruf
hidup pada suatu kalimat'''

a_string = "tasya seharwa"
lowercase = a_string.lower()
total = 0
for x in "atsy":
 jml = lowercase.count(x)
 total += jml
print(total)

#soal 2
'''kamu sebagai mahasiswa teknik informatika diminta untuk mengganti
semua huruf kecil pada kalimat ini 'makan apa aja pasti enak' menjadi
huruf besar'''

kalimat = 'makan apa aja pasti enak'
print(kalimat.upper())


