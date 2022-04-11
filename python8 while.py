angka = 0

while angka < 5:
    print("nilai angka adalah ", angka)
    angka += 1 #inkrement
print("di luar while")



# menggunkan boolean
start = True
angka = 0

while start:
     print("di dalam while")
     if angka == 50:
         start = False
         print("angka",angka ,"di temukan")
     angka += 1

