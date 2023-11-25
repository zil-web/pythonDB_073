import tkinter as tk
import sqlite3
from tkinter import messagebox

def simpan_data_ke_sqlite(Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas):

# Membuka atau membuat database SQLite
    conn = sqlite3.connect("DBTugas8.db")
    cursor = conn.cursor()

# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS Nilai_Siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Nama_Siswa TEXT,
                    Biologi INTEGER,
                    Fisika INTEGER, 
                    Inggris INTEGER,
                    Prediksi_Fakultas TEXT)''')

# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO Nilai_Siswa (Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas) VALUES (?, ?, ?, ?, ?)",
                    (Nama_Siswa, Biologi, Fisika, Inggris, Prediksi_Fakultas))

# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

top = tk.Tk()
top.title("Kelas B") #Untuk memberi nama judul
top.geometry("500x500") 
top.resizable(False, False)

def Prediksi_Fakultas(Biologi, Fisika, Inggris):
    if Fisika < Biologi > Inggris:
        return "Kedokteran"
    elif Biologi < Fisika > Inggris:
        return "Teknik"
    elif Biologi < Inggris > Fisika:
        return "Bahasa"
    else :
        return "Belum ada"


#Menampilkan fungsi
def show():
    namaMhs = NS1.get()
    matkul1 = B1.get()
    matkul2 = F1.get()
    matkul3 = I1.get()

    hasilMhs = f"Nama Mahasiswa: {namaMhs}"
    hasil1 = f"Mata Kuliah 1: {matkul1}"
    hasil2 = f"Mata Kuliah 2: {matkul2}"
    hasil3 = f"Mata Kuliah 3: {matkul3}"

    prediksi = Prediksi_Fakultas(matkul1, matkul2, matkul3)

    hasilPrediksi = f"Hasil Prediksi: {prediksi}"

    label_hasilMhs.config(text=hasilMhs)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)
    label_hasilprediksi.config(text=hasilPrediksi)

    if not matkul1 and not matkul2 and not matkul3 and not namaMhs:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlite(namaMhs, matkul1, matkul2,matkul3,prediksi)
        messagebox.showinfo("Info","Data Tersimpan")


# Label Judul
label_judul = tk.Label(top, text="Prediksi Prodi Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(top, labelanchor="n",pady=10, padx=10)
frame_input.pack()


# Label Nama Mahasiswa
NS = tk.Label(frame_input, text="Masukkan Nama Anda: ")
NS.grid(row=0, column=0, pady=10)
NS1 = tk.Entry(frame_input)
NS1.grid(row=0,column=1)

# Label Nilai Biologi
B = tk.Label(frame_input, text="Nama Mata kuliah Biologi: ")
B.grid(row=1, column=0, pady=10)
B1 = tk.Entry(frame_input)
B1.grid(row=1,column=1)

# Label Nilai Fisika
F = tk.Label(frame_input, text="Nama Mata kuliah Fisika: ")
F.grid(row=2, column=0, pady=10)
F1 = tk.Entry(frame_input)
F1.grid(row=2,column=1)

# Label Nilai Inggris
I = tk.Label(frame_input, text="Nama Mata kuliah Inggris: ")
I.grid(row=3, column=0, pady=10)
I1 = tk.Entry(frame_input)
I1.grid(row=3,column=1)

# Label Prediksi Hasil

# Tombol Hasil
btn_hasil = tk.Button(top, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(top,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_hasilMhs = tk.Label(frame_hasil, text="")
label_hasilMhs.pack()

label_hasil1 =  tk.Label(frame_hasil,text="")
label_hasil1.pack()

label_hasil2 =  tk.Label(frame_hasil,text="")
label_hasil2.pack()

label_hasil3 =  tk.Label(frame_hasil,text="")
label_hasil3.pack()

label_hasilprediksi = tk.Label(frame_hasil, text="")
label_hasilprediksi.pack()

top.mainloop()
