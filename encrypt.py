from tkinter import Tk, Button, Entry, Text, StringVar, END
from aes256 import encrypt

w = Tk()
#w.geometry("400x600")
w.resizable(False, False)
w.title("Encryptor")

def encrypttext():
    if rawtext.get(1.0, "end-1c").strip() != "" and passwordvariable.get().strip() != "":
        encrypted = encrypt(rawtext.get(1.0, "end-1c"), passwordvariable.get()).decode()
        rawtext.delete("1.0", END)
        rawtext.insert(END, encrypted)
        passwordvariable.set("")
    else:
        print("Please enter text in both fields.")

passwordvariable = StringVar()
rawtext = Text(w, height=28)
rawtext.pack()
passwordentry = Entry(w, textvariable=passwordvariable, show="*")
passwordentry.pack(fill="x")
encryptbutton = Button(w, text="Encrypt", command=encrypttext)
encryptbutton.pack(fill="x")
w.mainloop()
