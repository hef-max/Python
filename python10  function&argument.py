# fungsi dengan menggunakan arguments sederhana
def siswa(nama):
    print('siswa ini bernama', nama)
siswa('mario')

# fungsi ini menggunakan keywords arguments
def guru(nama,pelajaran):
    print('guru ini bernama: ',nama)
    print('mengajar mata pelajaran: ',pelajaran)
guru(nama='pak tomi',pelajaran='matematika')
guru(pelajaran='olahraga',nama='pak fadil') #seperti ini juga boleh
guru('fisika', 'pak hendi') # nah yang kaya gini yang ga boleh cause no acurat

def satpamsekul(nama,shift='malam',sifat='galak'):
    print('satpam ini bernama: ',nama)
    print('shift: ',shift)
    print('sifatnya: ',sifat)
satpamsekul('rohid') # kalo seperti ini boleh, cause dibagian var sudah di program