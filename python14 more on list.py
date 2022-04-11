Barang = ['Topi', 'Baju', 'Jaket', 'Kaos']
print(Barang)

# beberapa methode yang bisa digunakan untuk memanipulasi list
# methode untuk menambah list
Barang.append('mouse') # untuk menambah data/anggota
print(Barang)

Barang.extend('Keybord') # menambahkan tapi berbeda
print(Barang)


Barang.insert(3,'Topi') # menambahkan barang with index
print(Barang)

print(100*'=')
# methode untuk menghitung anggota(list)
jumlahTopi = Barang.count('Topi')
print('jumlah topi yang ada di barang adalah', jumlahTopi)

# meremove data
Barang.remove('Topi')
print(Barang)

Barang.reverse() # membalikan anggota, (kaya edit video tuh)
print(Barang)

print(100*'=')
stuff = Barang.copy() # menyalin anggota(list) ke var baru [list BARU]
stuff.append('Buku')
print(stuff)