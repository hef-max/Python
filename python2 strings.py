text1 = 'jalan-jalan di hari sabtu'

text2 = 'jalan-jalan di hari jum\'at' #ini adalah cara ke satu dengan (\')

text3 = "jalan-jalan di hari jum'at" # cara ke dua dengan diawali (" ")

text4 = 'ary bertanya: "kemarin lu kemana bro?"'

text5 = "raju menjawab: \"gw kemarin ke hgl\""

text6 = 'ary bertanya: "kemarin lu kemana bro?" \nraju menjawab: "gw kemarin ke hgl"' # (\n) untuk baris baru

text7 = """
ary : "kemarin lu kemana bro?"
raju : "gw kemarin ke hgl"
ary : "ngapin bro?"
raju : "makan baso"
""" #lebih mempermudah dari pada text" di atas

text8 = r'C:\nyoto' #(r) adalah raw string untuk menghilangkan contoh f(\)

print(text8)
print(5*"wk") # untuk mepermudah/mempersingkat sc dengan mengkalinya
print('kue' 'pukis') #seperti ini juga bisa
print(text1 + text2)
print(text4,text5)