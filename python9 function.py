# membuat fungsi sederhana

def suaraayam():
    print('kukuruyuk!!')
def hargaayam():
    suaraayam() #bisa juga disini manggilnya
    print('harga ayam 1 adalah 20.000')
def hargaTotAyam(kg):
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'kg ayam adalah', hargaTotal)

hargaayam() #maka akan menyebutkan 2 definisi sekaligus
hargaTotAyam(2) #masukan dengan input