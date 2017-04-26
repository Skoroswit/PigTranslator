import tkinter, sys
from tkinter import messagebox

def progg():
    pyg = 'ay'
    original = e.get()
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word+first+pyg
        new_word = new_word[1:]
        l2.config(text=new_word)
    else:
        l2.config(text="error")
        messagebox.showinfo(title="Uwaga", message="Wprowadź poprawne słowo")

def endprog():
    sys.exit()

main = tkinter.Tk()

e = tkinter.Entry(main, justify="center")
l = tkinter.Label(main, text = "Wprowadź słowo do tłumaczenia:")
b1 = tkinter.Button(main, text = "Tłumacz", command = progg)
l2 = tkinter.Label(main, text ="...")
b = tkinter.Button(main, text = "Zakończ program", command = endprog)

l.pack()
e.pack()
b1.pack()
l2.pack()
b.pack()

main.mainloop()