# scope var local
namaKucing = 'catie'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya rubah nama kucing', namaKucing)

rubahNamaKucing('alex')
print('nama kucing saya menjadi', namaKucing)

print(100*'=')

# scope var global
namaCat = 'katty'
makananCat = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaCat
    namaCat = namaBaru
    print('saya rubah nama kucing', namaCat)

def makananKucing(makanan,nama):
    global namaCat,makananCat
    namaCat = nama
    makananCat =  makanan

rubahNamaKucing('alex')
makananKucing('whiskes','gabi')
print('menjadi', namaCat, 'dan makan', makananCat)
