# menangkap error
print('ini adalah pembagian')

while True:
    try:
        penyebut = int(input('masukan angka pertama: '))
        pembilang = int(input('masukan angka kedua:'))
        hasil = penyebut/pembilang
        break
    # tata cara menangkap error
    except ValueError:
        print('yang anda masukan bukan angka')
    except ZeroDivisionError:
        print('angka pembilang yang anda masukan adalah nol')
    except Exception as err:
        print(err)
print('hasil pembagian =', hasil)

