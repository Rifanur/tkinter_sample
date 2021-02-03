# p16 tk24.pyw

import tkinter as tk
def get_selpoint():
    sel_start = txt.index('sel.first')
    sel_end = txt.index('sel.last')
    lb['text'] = 'sel_start:{},sel_end:{}'.format(sel_start,sel_end)

root = tk.Tk()
lb = tk.Label()
txt = tk.Text(height=5,width=30)
bt = tk.Button(text='selected range',command=get_selpoint)
[widget.pack()for widget in (lb,txt,bt)]

root.mainloop()
