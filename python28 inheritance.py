class ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.tranmisi = transmisi
        self.daerah = daerah
        
    def cek_id_ojek(self):
        print('nama:',self.nama,'\nmotor:',self.tranmisi,'\ndaerah:',self.daerah)

class gojek(ojek):

    def cek_id_ojek(self):
        print('cek aplikasi')


order = ojek(nama='hefry', transmisi='manual',daerah='bandung')
order2 = gojek('heru', 'manual', 'bogor')

order.cek_id_ojek()
order2.cek_id_ojek()
