from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# membuat array of objects
hunians = []

# lakukan instansiasi dan isi data
hunians.append(Apartemen("Nelly Joy", 3, 3, "35 m2", "Apartement Leaf No 301"))
hunians.append(Rumah("Sekar MK", 5, 2, "72 m2", "Cluster Dahlia"))
hunians.append(Indekos("Bp. Romi", "Cahya", "Rp 1.600.000"))
hunians.append(Rumah("Satria", 5, 4, "40 m2", "Cluster Primrose"))
hunians.append(Apartemen("Zahra F", 1, 2, "25 m2", "Apartement Hux No 101"))
hunians.append(Indekos("Ibu Mega","Alya", "Rp 800.000"))

# membuat instance objek tkinter
root = Tk()
# mengatur judul aplikasi
root.title("Latihan 9 DPBO Python")
# mengatur jendela ukuran tkinter
root.geometry("600x500") 

# fungsi untuk menampilkan detail data
def details(index):
    
    # membuat jendela terpisah
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # membuat label frame data residen
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan detail
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

# fungsi untuk menampilkan data residen
def show_data():

    # membuat instance objek tkinter kembali karena yg sebelumnya sudah di destroy
    root = Tk()
    root.title("Data Seluruh Residen")
    root.geometry("600x300") 

    # membuat label frame untuk data seluruh residen
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    # membuat label frame untuk opsi button
    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # membuat button
    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)
    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # loop untuk menampilkan data
    for index, h in enumerate(hunians):
        
        # membuat label frame untuk urutan data ke berapa
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        # membuat label frame untuk data residen
        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        # membuat label frame untuk nama pemilik/penghuni residen
        # kalau residen bukan Indekos maka yg ditampilkan itu atribut nama pemilik
        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        # kalau residen Indekos maka yg ditampilkan itu atribut nama penghuni
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        # button untuk details
        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# fungsi saat tombol "Lihat Data" dipencet
def destroy_and_show_data():
    # menutup root
    root.destroy()
    # memanggil fungsi untuk menampilkan data residen
    show_data()

# membuat landing page
landing_page_title = Label(root, text="Selamat Datang di Pesona Residential", font=("Helvetica", 18, "bold"))
landing_page_title.pack(pady=20)

# kalimat-kalimat yang ditampilkan di landing page
sentence1 = Label(root, text="Aplikasi ini menyediakan data-data penghuni residensial kami.", font=("Helvetica", 12))
sentence1.pack()
sentence2 = Label(root, text="Untuk melihat lebih lanjut, klik tombol 'Lihat Data'", font=("Helvetica", 12))
sentence2.pack(pady=10)

# menampilkan gambar
gambar = PhotoImage(file="D:\\College\\SEM 4\\DPBO\\latihan\\latihan9\\image\\residensial.png")
gambar_kecil = gambar.subsample(2, 2)  # mengurangi ukuran gambar menjadi setengah
w1 = Label(root, image=gambar_kecil).pack(pady=10)

# tombol "Lihat Data"
b_show_data = Button(root, text="Lihat Data", command=destroy_and_show_data)
b_show_data.pack(pady=10)

# aplikasi akan terus berjalan sampai user memencet opsi "Exit"
root.mainloop()
