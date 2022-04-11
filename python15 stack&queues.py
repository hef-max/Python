# stack/tumpukan
tumpukan = [1,2,3,4,5,6]
print("data sekarang:", tumpukan)

# menambahkan data
tumpukan.append(7)
print("data masuk:",7)
tumpukan.append(8)
print("data masuk:",8)
print("data sekarang:", tumpukan)

# mengeluarkan antrian diakhir(tehnik stacking)
out = tumpukan.pop()
print("data keluar:",out)
print("data sekarang:", tumpukan)

print(100*'=')

# queues/tumpukan
from collections import deque

antrian = deque([1,2,3,4,5,6]) #why menggunaknan deque? cause lebih muda menghilangkan/menambah data di awal
print("data sekarang:", antrian)

# menambahkan data
antrian.append(7)
print('data masuk:',7)
antrian.append(8)
print('data masuk:',8)
print('data sekarang:',antrian)

# mengurangi antrian di awal
out =  antrian.popleft()
print('data keluar:',out)
print('data sekarang:',antrian)


