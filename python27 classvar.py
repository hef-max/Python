class mahasiswa():

    jumlah_mahasiswa =  0
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

        mahasiswa.jumlah_mahasiswa += 1

# main program

# jadi setiap mahasiswanya/namanya bertambah angkanya juga bertambah
otong = mahasiswa('atong surotong', 181920001)
yusuf = mahasiswa('yusuf lesmana', 181920002)
sekar = mahasiswa('sekar nanti', 181920003)

print(mahasiswa.jumlah_mahasiswa)



