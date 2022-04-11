# membuat GUI sederhama
import tkinter

window = tkinter.Tk()


def event_tekan():
    label2 = tkinter.Label(window, text='1')
    label2.pack()


label = tkinter.Label(window, text='hello, saya adalah program sederhana menggunakan GUI')
tombol = tkinter.Button(window, text='tekan aku', command=event_tekan)

label.pack()
tombol.pack()
window.mainloop()
