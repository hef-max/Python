nilai = 70

if nilai == 70:
    print("nilai anda adalah = ", nilai)
if nilai == 60:
    print("nilai anda adalah = ", nilai)

print(25*'=')


nilai = 49

print(nilai)

if 80 <= nilai <= 100:
    print('nilai anda adalah A')
elif 70 <= nilai <= 80:
    print('nilai anda adalah B')
elif 60 <= nilai <= 70:
    print('nilai anda adalah C')
elif 50 <= nilai <= 60:
    print("nilai anda adalah T, segera perbaiki")
else:
    print('anda tidak lulus mata kuliah ini!!!!')



print(50*"=")
print("operator logika untuk list dan string")
print(" ")

gorengan = ["pisang molen", "bakwan", "getu", "combro", "pisang goreng", "pukis", "cireng"]
beli = "bakwan"

if beli in gorengan:
    print('Mamng bilang: "ya saya jual',beli,'"')
if not beli in gorengan:
    print(beli,"kaga jualan")


karakter = "n"

if karakter in beli:
    print("ada", karakter,"di",beli)
else:
    print("kaga ada", karakter, "di",beli)


