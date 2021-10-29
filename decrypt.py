from tkinter import Tk, Button, Entry, Text, StringVar, END
from aes256 import decrypt

w = Tk()
w.resizable(False, False)
w.title("Decryptor")

def decrypttext():
    if rawtext.get(1.0, "end-1c").strip() != "" and passwordvariable.get().strip() != "":
        decrypted = decrypt(rawtext.get(1.0, "end-1c"), passwordvariable.get()).decode()
        rawtext.delete("1.0", END)
        rawtext.insert(END, decrypted)
        passwordvariable.set("")
passwordvariable = StringVar()
rawtext = Text(w, height=28)
rawtext.pack()
passwordentry = Entry(w, textvariable=passwordvariable, show="*")
passwordentry.pack(fill="x")
decryptbutton = Button(w, text="Decrypt", command=decrypttext)
decryptbutton.pack(fill="x")
w.mainloop()