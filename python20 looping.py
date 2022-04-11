band = ['coldplay',
        'coldplay',
        'justin bieber',
        'billi elise']
lagu = ['the scientist',
        'yellow',
        'holy',
        'lovely']

# menggunakan enumerete
for index,var in enumerate(band):
    print(index,':',var)

#zip (menggabungkan list)
for nama_band,lagunya in zip(band,lagu):
    print(nama_band, 'menyanyikan lagu:', lagunya)

print(100*'=')

#set
playlist = {'lovely','yellow','the scientist','death bad'}

for lagu in sorted(playlist):
    print(lagu)

print(100*'=')

#dictionary
playlist2 = {'coldplay': 'the scientist',
        'powfu': 'deat bad',
        'justing bieber':'holy',
        'billi elise':'lovely'}

for lagu in playlist2.items():
    print(lagu)
for lagu in playlist2.values():
    print(lagu)