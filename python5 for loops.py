# list sebagai iterable
gorengan = ["bakwan", "cireng", "tahu isi", 'tempe goreng', 'ubi goreng']

for g in gorengan: #kalau kau bingung apa itu g? g itu variable baru.. dia(mesin) akan melakukan loop
    print(g)

# string sebagai iterable
bakwan = "bakwan"

for i in bakwan: # dia(mesin) akan mengeja
    print(i)

# for di dalam for

buah = ["semangka","pisang",'jeruk','angggur']
sayur = ['kangkung','wortel','tomat','kentang']

Daftar_Belanja = [gorengan, buah, sayur]

for DaftarBelanja in Daftar_Belanja: #merapikan list
    print(DaftarBelanja)
    for komponen in DaftarBelanja: #untuk menjabarkan setiap komponen di dalam list
        print(komponen)
