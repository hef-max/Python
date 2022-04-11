num = 2

for i in range(10): #sama semacem dijs yg (for i = 0; i < 10;) klo range ditambah (,) lagi maka akan aada i++
    print(i)
    if i is num:
        print("angka",num,"di temukan")
        break
else: #di luar if.. sama dengan  for
    print("angka tidak ditemukan")