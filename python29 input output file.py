# input output file

# membuat file text

#-----------------------------------------------------
# w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan buat file baru
# r = read mode / hanya bisa baca
# a = appending mode / menambahkan data diakhir baris
# r+ = write and read mode
#---------------------------------------------------

# membuat file txt

file = open('data.txt', 'w')

file.write('ini adalah data text yang dibuat dengan menggunakan python')
file.write('\nini baris kedua ')
file.write('\nini baris ketiga')
file.write('\nini baris keempat')

file.close() # if u make file\write, u have to pake close()

# membaca file txt
file2 = open('data.txt', 'r')

print(file2.read())

# menambahkan data
file3 = open('data.txt', 'a')

file3.write('\nbaris ini di buat menggunakan mode append')

file3.close()

