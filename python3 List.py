Data = [1,4,9,16,25,36,49,64]

#mengakses list
subdata1 =  Data[2]
subdata2 =  Data[-3]

#memotong list
subdata3 = Data[2:4]
subdata4 = Data[4:]

Data2 = [100,200,300,400,500,600]

#menambah list
Data3 = Data + Data2

#cara 1
#merubah content dari list
Data[4] = 26   #merubah data ke 4 menjadi 87, dan ini juga teknik termudah

#cara 2
#meencopy list ke variable baru
a = Data[:]
a[3] = 18

#cara 3
# merubah data list menggunakan metode slicing
Data[3:5] = [13,15]

# list dalam list
x = [Data,Data2]

# meng akses list dalam multidimensional list
y = x[0][4] # yang pertama pilih list nya antara 0 dan 1(karena listnya ada 2) lihat di [x], ke dua pilih baris ke berapa

# Methods untuk list
Data.append(90) #untuk menambahkan data
Data2.append(700)

# Function yang bisa kita gunakan kepada list
panjang_list = len(Data) #untuk menghitung jumlah data yang ada di list
