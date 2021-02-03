import tkinter as tk
root = tk.Tk()
root.title('geometry')
root.geometry('350x350')
lb = tk.Label(text='Label - 1')
bt = tk.Button(text = 'Button -1')
lb.pack()
bt.pack()
root.mainloop()