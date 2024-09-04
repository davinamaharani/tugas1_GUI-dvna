import tkinter as tk

def RumusPersegiPanjang():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    luas = panjang * lebar
    label_hasil.config(text=f"Luas Persegi Panjang: {luas}")

# jendela
jendela = tk.Tk()
jendela.title("TugasGUI - Davina Maharani")

label_rumus = tk.Label(jendela, text="HITUNG LUAS PERSEGI PANJANG!", fg="#2c788e")
label_rumus.pack()

logo = tk.PhotoImage(file="persegipnjng.png")
WLableImage = tk.Label(image=logo)
WLableImage.pack()

#label panjang
label_panjang = tk.Label(jendela, text="panjang:")
label_panjang.pack()
entry_panjang = tk.Entry(jendela)
entry_panjang.pack()

#label lebar
label_lebar = tk.Label(jendela, text="Lebar:")
label_lebar.pack()
entry_lebar = tk.Entry(jendela)
entry_lebar.pack()

#membuat label dan entry untuk input
button = tk.Button(jendela, text="Hitung Luas", command=RumusPersegiPanjang)
button.pack()

label_hasil = tk.Label(jendela, text="")
label_hasil.pack()

jendela.mainloop()