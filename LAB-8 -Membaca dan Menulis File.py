#Tasya Setyo Harwati
#71200580

#Soal 1
'''kamu adalah seorang mahasiswa teknik informatika. kamu
diminta bantuan oleh temanmu yang bukan mahasiswa teknik 
informatika untuk membuka dan membaca file txt yang dia temukan
dari sebuah game misteri.'''

handle = open("Pantun.txt","r")
print(handle.read())
handle.close()

#soal 2
'''kamu adalah seorang mahasiswa teknik informatika yang sedang
iseng dalam mengisi waktu luang. kamu berencana ingin menulis sepenggal
lagu korea pada file txt yang masih kosong atau belum terisi.'''

handle = open("Love Scenario.txt","w")
tulisan = "Sarangeul haeda uriga manna Jiuji moshal chueogi dwaeda Bolmanhan mellodeurama Gwaenchanheun gyeolmal Geugeomyeon dwaeda neol saranghaeda Uriga mandeun love scenario\n"
handle.write(tulisan)
handle.close()

#soal 3
'''kamu adalah seorang mahasiswa teknik informatika. kamu
diminta bantuan oleh ayahmu untuk membuka dan membaca file txt yang diberikan
oleh ibumu yang lulusan teknik informatika.'''

handle = open("Mylife.txt","r")
print(handle.read())
handle.close()
