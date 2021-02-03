# tk21.pyw

import tkinter as tk
root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
strvar.set('Hello Word')
en.pack()

root.mainloop()