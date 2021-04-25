#Tasya Setyo Harwati


#soal 1
'''kamu seorang mahasiswa teknik informatika sedang mengisi waktu luang. kamu
ingin menambahkan nama negara pada seseorang dengan tipe data menggunakan
dictionary '''

my_dict = {'nama':'Zerolima', 'umur':25} 
my_dict['umur'] = 25 
print(my_dict) 

my_dict['Negara'] = 'Indonesia' 
print(my_dict) 

#soal 2
'''kamu seorang mahasiswa teknik informatika sedang mengisi waktu luang ingin
membuat program untuk menghitung huruf dari kalimat atau kata yang akan user
input pada program yang kamu buat dengan tipe data dictionary'''

teks = input('Tuliskan kata: ').lower()
dictionary_huruf = {
  'a': 0,
  'b': 0,
  'c': 0,
  'd': 0,
  'e': 0,
}
for huruf in dictionary_huruf.keys():
  dictionary_huruf[huruf] = teks.count(huruf)
total_huruf = sum(dictionary_huruf.values())

print(f'Total karakter: {len(teks)}')
print(f'Total huruf: {total_huruf}')
print(f"""\
  a -> {dictionary_huruf['a']}
  b -> {dictionary_huruf['b']}
  c -> {dictionary_huruf['c']}
  d -> {dictionary_huruf['d']}
  e -> {dictionary_huruf['e']}\
""")


