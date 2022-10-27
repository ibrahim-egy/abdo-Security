from tkinter import *


def rsa():
    def encrypt_rsa():
        p = int(ptk.get())
        q = int(qtk.get())
        e = int(etk.get())
        m = int(mtk.get())
        n = p * q
        phi_n = (p - 1) * (q - 1)
        phi_n1 = phi_n
        while True:
            d = str((phi_n1 + 1) / e)
            j = 0
            for i in range(len(d)):
                if d[i] == '.':
                    j = d[i + 1]
                    break

            if j != '0':
                phi_n1 += phi_n
            else:
                break
        c = (m ** e) % n
        canvas.itemconfig(out, text=f"Cypher message: {c}")

    canvas.delete('all')
    elgamal_btn = Button(text="ElGAMAL", width=10, height=2, bg='#C69B7B', command=elgamal, highlightthickness=0)
    elgamal_btn.grid(column=1, row=1)
    rsa_button.destroy()
    ptk = Entry(window)
    qtk = Entry(window)
    etk = Entry(window)
    mtk = Entry(window)
    canvas.create_window(250, 10, window=ptk)
    canvas.create_window(250, 40, window=qtk)
    canvas.create_window(250, 70, window=etk)
    canvas.create_window(250, 100, window=mtk)
    canvas.create_text(180, 10, text="P: ", font='Courier 10 bold', fill='black')
    canvas.create_text(180, 40, text="Q: ", font='Courier 10 bold', fill='black')
    canvas.create_text(180, 70, text="E: ", font='Courier 10 bold', fill='black')
    canvas.create_text(160, 100, text="Message: ", font='Courier 10 bold', fill='black')

    out = canvas.create_text(250, 200, text=f"", font='Courier 15 bold')

    encrypt_button = Button(text="Encrypt", width=10, height=2, bg='#C69B7B', command=encrypt_rsa, highlightthickness=0)
    encrypt_button.grid(column=0, row=1)


def elgamal():
    def encrypt_elgamal():

        a = int(atk.get())
        q = int(qtk.get())
        m = int(mtk.get())
        xa = int(xatk.get())
        k = int(ktk.get())

        ya = (a ** xa) % q
        kc = (ya ** k) % q

        c1 = (a ** k) % q
        c2 = (kc * m) % q
        i = 1
        while True:

            if ((kc * i) % q) == 1.0:
                break
            i += 1
        m = (c2 * i) % q
        canvas.itemconfig(out, text=f"K inverse: {i} \n message: {m}")

    canvas.delete('all')
    rsa_btn = Button(text="RSA", width=10, height=2, bg='#C69B7B', command=rsa, highlightthickness=0)
    rsa_btn.grid(column=0, row=1)

    encrypt_button = Button(text="Encrypt", width=10, height=2, bg='#C69B7B', command=encrypt_elgamal,
                            highlightthickness=0)
    encrypt_button.grid(column=1, row=1)

    atk = Entry(window)
    qtk = Entry(window)
    xatk = Entry(window)
    mtk = Entry(window)
    ktk = Entry(window)
    canvas.create_window(250, 10, window=atk)
    canvas.create_window(250, 40, window=qtk)
    canvas.create_window(250, 70, window=xatk)
    canvas.create_window(250, 100, window=mtk)
    canvas.create_window(250, 130, window=ktk)
    canvas.create_text(180, 10, text="A: ", font='Courier 10 bold')
    canvas.create_text(180, 40, text="Q: ", font='Courier 10 bold')
    canvas.create_text(180, 70, text="xa: ", font='Courier 10 bold')
    canvas.create_text(160, 100, text="Message: ", font='Courier 10 bold')
    canvas.create_text(180, 130, text="k: ", font='Courier 10 bold')
    out = canvas.create_text(250, 200, text=f"", font='Courier 15 bold')


# GUI
window = Tk()
window.title("MSA CS Security Project")
window.config(width=500, height=400, bg="#F3E0B5", padx=20, pady=20)

canvas = Canvas(window, width=500, height=300, bg="#F3E0B5", bd=0, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

canvas.delete('all')
canvas.create_text(250, 70, text="Encryption App", font='Courier 15 bold')
canvas.create_text(250, 110, text="Designed and implemented by Abdelrahman and Adham", font='Courier 12 bold')
canvas.create_text(250, 200, text="Please Choose A Methode", font='Courier 15 bold')

rsa_button = Button(text="RSA", width=10, height=2, bg='#C69B7B', command=rsa, highlightthickness=0)
rsa_button.grid(column=0, row=1)

elgamal_button = Button(text="ElGAMAL", width=10, height=2, bg='#C69B7B', command=elgamal, highlightthickness=0)
elgamal_button.grid(column=1, row=1)
window.mainloop()
