from tkinter import *
from tkinter import filedialog

# from tkFileDialog import askopenfilename
# import tkFileDialog as filedialog

def callback():
    name = filedialog.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()