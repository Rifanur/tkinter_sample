import tkinter as tk

def action_btn_press():
    print('Button was pressed!')

root = tk.Tk()
root.title('Weight+Action')
root.geometry('350x350')
lb = tk.Label(text='Label - 1')
bt = tk.Button(text = 'Button -1',command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()