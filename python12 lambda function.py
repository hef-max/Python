# lebih simpennya lambda lebih simpel dari def
# membuat fugsi dengan lambda

#ini contoh with def
def kali(a,b):
    c = a*b
    return c
hasil = kali(4,4)
print(hasil)

# bisa lebih simpel dengan lambda
# membuat anonymouse function with lambda
kali =  lambda a,b: a*b
hasil = kali(3,3)
print(hasil)

argumen = lambda  argument: print(argument)

argumen('test')


print(100*"=")



def penjumlahan(a,b):
    c = a + b
    return c

print(penjumlahan(2,5))




