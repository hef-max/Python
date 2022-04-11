class siswa():

    def __init__(self,input_nama,nim):
        self.nama = input_nama #public
        self.nim = nim #public
    def learn(self,kondisi):
        print('sedang belajar di kelas ini', kondisi)
    def sleep(self):
        print('sedang tidur di kelas')

# main program

otong = siswa('otong surotong', 123)

otong.learn('dengan giat')
print(otong.nama)
print(otong.nim)
otong.nama = 'atang'
print(otong.nama)

