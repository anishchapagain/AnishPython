from tkinter import *
import sys
def hello(event):
    print("Single Click, Button-l") 
def quitOut(event):                           
    print("Double Click, so let's stop") 
    root.destroy() #close main window sys.exit(1) or root.quit()

root = Tk()

widget = Button(root, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quitOut) 
widget.mainloop()
