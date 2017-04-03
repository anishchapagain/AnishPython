"""
http://nullege.com/codes/search/tkinter
"""

from tkinter import *
from tkinter import messagebox

def process():
    if(e1.get()!='' or e2.get()!=''):
        messagebox.showinfo(title="Title",message=e1.get())
        if 'User' in e1.get():
            if messagebox.askyesno(title="Asking Yes No",message="Are you sure about Login Details"):
                if messagebox.showinfo(title="YES",message="User is Sure"):
                    messagebox.showinfo(title="YES",message="LOGIN SUCCESSFUL")
                    root.destroy()
                    
            else:
                messagebox.showinfo(title="No",message="User is not Sure")
                             

root = Tk()
root.maxsize(400,200)
root.minsize(200,150)
# root.resizable(width=False,height=False)
#title, message

Label(root, text="Username:").grid(row=0)
Label(root, text="Password:").grid(row=1,pady=10)
e1 = Entry(root,width=50)
e2 = Entry(root,width=50,show='$')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

print(e1.get())
#messagebox.showerror(title="Title Again",message=e2.get())
print(e2.get())

Button(root,text="Process",command=process).grid(row=2,column=1,sticky=W,padx=10)
Button(root,text="Quit",command=root.destroy).grid(row=2,column=1,sticky=W,padx=100)

#icon: ERROR , INFO, QUESTION, WARNING
#ABORTRETRYIGNORE, OK, OKCANCEL, RETRYCANCEL, YESNO, or YESNOCANCEL


# messagebox.showwarning(title="Title Again",message="showwarning")

# messagebox.askquestion(title="Title Again",message="askquestion")
# messagebox.askokcancel(title="Title Again",message="askokcancel")
# messagebox.askyesno(title="Title Again",message="askyesno")
# messagebox.askretrycancel(title="Title Again",message="askretrycancel")
mainloop()