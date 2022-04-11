# list
ganjil = [1,3,5,7,9]

# tuple # can't change
genap = (2,4,6,8,10)

# to knowing type data
print(type(ganjil))
print(type(genap))

# untuk mengetahui apa saja with type data list and tuple
print(dir(ganjil))
print(dir(genap))

print(100*'=')

# cara mengetahui size type data
import sys

data_list = [1,2,3,4,5,'pisang','apel','anggur', False]
data_tuple = (1,2,3,4,5,'pisang','apel','anggur',False)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print('besar data list:', besar_datalist)
print('besar data tuple:', besar_datatuple)

print(100*'=')

# cara mengecek waktu type data
import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]")
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)")

print('waktu data list:',data_list)
print('waktu data tuple:',data_tuple)