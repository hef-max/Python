class siswa():

    jurusan ='informatika'
    __nilai = 0  # be privet (cant not in acces from luar)
    def __init__(self, input_nama, nim):
        self.nama = input_nama  # public
        self.nim = nim  # public

    def uts(self,nilai):
        self.__nilai += nilai
    def uas(self,nilai):
        self.__nilai += nilai
    def chech_setatus(self):
        if self.__nilai <= 50:
            print(self.nama,'anda tidak lulus')
        else:
            print(self.nama,'anda lulus')

# main program

otong = siswa('otong surotong', 181920001) #instense
yusuf = siswa('yusuf lesamana', 181920002) #instense

otong.uts(10)
otong.uas(30)
otong.chech_setatus()

yusuf.uts(40)
yusuf.uas(20)
yusuf.chech_setatus()
