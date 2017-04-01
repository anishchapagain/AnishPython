from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

def quit(event):                           
    print("Double Click, so let's stop") 
    master.destroy()

master = Tk() 

widget = Button(master, text='Quit Me - Double Click')
widget.pack()
widget.bind('<Double-1>', quit) 

whatever_you_do = """Whatever you do will be insignificant, but it is very important that you do 
it.\n(Mahatma Gandhi)"""
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
master.mainloop()