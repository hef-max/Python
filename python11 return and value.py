# fungsi with return value

def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah = ',total)
    return total #untuk menegembalikan lagi

print(kuadrat(6)) #kan biasanya langsung pakai kuadrat() dengan return bisa kaya gini
#kuadrat(5) #tanpa return

print(100*'=')

# fungsi with return value and multiple argumen

def tambah(argumen,argumen2):
    total = argumen + argumen2
    print('hasil dari', argumen, '+', argumen2, '=', total)
    return total # bisa juga dengan list
def kali(argumen,argumen2):
    total = argumen * argumen2
    print('hasil dari', argumen, 'x', argumen2, '=', total)
    return total

c = kali(4, tambah(3,4)) # dia akan mengeksekusi yang di dalam kurung duluan
print(c) # karena dengan return bisa juga manggil dengan hasilnya saja
