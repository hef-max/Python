import module

print(module.data)

module.build()

print(100*'=')

#-------------------------
import module

module.tambah(3,3)
module.kurang(3,2)

print(100*'=')
# can also with like this
import module as math # (as) itu sama seperti (==) jika di if

math.tambah(5,3)
math.kurang(5,2)
print(100*'=')

# can also like this
from module import tambah, kurang

tambah(5,5)
kurang(10,4)
print(100*'=')

# or like this
from module import * # for all calld

build()
tambah(1,3)
kurang(3,2)

