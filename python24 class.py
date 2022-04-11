# different[class] with to function(def)
class siswa():
    nama = 'nama'
    def learn(self,kondisi): # self is name yang ada di ucup\yusuf [(def) here calld methode]
        print(self.nama,'sedang belajar di kelas ini', kondisi)
    def sleep(self):
        print(self.nama,'sedang tidur di kelas')

name = siswa() # name adalah siswa()[class]
name1 = siswa()

name.nama = 'ucup'
name1.nama = 'yusuf'

print(name.nama)
print(name1.nama)
#---------------
print(100*'=')
#---------------
name.learn('dengan giat') # "dengan giat" is kondisi
name1.sleep()
print(siswa)
