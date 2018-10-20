#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 15, 2018 12:18:17 AM IST  platform: Windows NT

import sys
import sqlite3
import tkinter.messagebox


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

conn = sqlite3.connect("Student.db")

cur = conn.cursor()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Student_Portal (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Student_Portal(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Student_Portal (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_Portal():
    global w
    w.destroy()
    w = None


class Student_Portal:
     def add_comannd(self):
         with conn:
             register=self.RegisterText.get('1.0',END)
             first=self.firstText.get('1.0',END)
             last=self.lastText.get('1.0',END)
             depart=self.departmentText.get('1.0',END)
             year=self.YearText.get('1.0',END)
             if (register == '\n' or first == '\n' or last == '\n' or depart == '\n' or year == '\n'):
                 tkinter.messagebox.showinfo("Alert","Please fill all the fields")
             else:
                 cur.execute("INSERT INTO Student_Details VALUES (?,?,?,?,?)", (int(register),first,last,int(depart),int(year)))
                 tkinter.messagebox.showinfo("Success","Details for "+str(first)+" "+str(last)+" is added")

             self.view()
             self.showListbox.delete(0, END)
             self.showListbox.insert(END, (register,first,last,depart,year))
             self.view_command()

     def view(self):
         return conn.execute("SELECT * FROM Student_Details")

     def update(self, register, first, last, depart, year):
         cur.execute("UPDATE Student_Details SET Req_No=?, First_Name=?, Last_Name=?, D_No=?, year=? WHERE Req_No=?", (register, first, last, depart, year, register))
         self.view()
         self.view_command()
         
     def update_command(self):
         register=self.RegisterText.get('1.0',END)
         first=self.firstText.get('1.0',END)
         last=self.lastText.get('1.0',END)
         depart=self.departmentText.get('1.0',END)
         year=self.YearText.get('1.0',END)
         if (register == '\n' or first == '\n' or last == '\n' or depart == '\n' or year == '\n'):
             tkinter.messagebox.showinfo("Alert","Please give all the details")
         else:
             self.update(int(register),first,last,int(depart),int(year))
             tkinter.messagebox.showinfo("Success","Details for "+str(first)+" "+str(last)+" is updated")

     def delete(self, register):
         cur.execute("DELETE FROM Student_Details WHERE Req_No=?", (register,))
         conn.commit()
         self.view()
         self.view_command()

     def delete_command(self):
         register=self.RegisterText.get('1.0',END)
         if (register == '\n'):
             tkinter.messagebox.showinfo("Alert","Please give Register Number")
         else:
             self.delete(int(register))
             tkinter.messagebox.showinfo("Success","Details for "+str(register)+" is deleted")
         

     def view_command(self):
         self.showListbox.delete(0, END)
         for row in self.view():
             self.showListbox.insert(END, row)

     def get_selected_row(self,event):
         global selected_tuple
         index = self.showListbox.curselection()[0]
         selected_tuple = self.showListbox.get(index)
         e1.delete(0, END)
         e1.insert(END, selected_tuple[1])
         e2.delete(0, END)
         e2.insert(END, selected_tuple[2])
         e3.delete(0, END)
         e3.insert(END, selected_tuple[3])


     def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI Light} -size 12 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("598x448+342+115")
        top.title("Student Portal")
        top.configure(background="#909b98")
        top.configure(cursor="based_arrow_up")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.0, rely=0.0, relheight=0.993, relwidth=0.995)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=595)

        self.Label1 = Label(self.TFrame1)
        self.Label1.place(relx=0.067, rely=0.09, height=31, width=94)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(text='''First Name''')

        self.Label2 = Label(self.TFrame1)
        self.Label2.place(relx=0.067, rely=0.18, height=31, width=94)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify=LEFT)
        self.Label2.configure(text='''Last Name''')

        self.Label3 = Label(self.TFrame1)
        self.Label3.place(relx=0.067, rely=0.27, height=31, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify=LEFT)
        self.Label3.configure(text='''Department''')

        self.Label4 = Label(self.TFrame1)
        self.Label4.place(relx=0.067, rely=0.36, height=31, width=84)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify=LEFT)
        self.Label4.configure(text='''Year''')

        self.firstText = Text(self.TFrame1)
        self.firstText.place(relx=0.269, rely=0.112, relheight=0.054
                , relwidth=0.276)
        self.firstText.configure(background="white")
        self.firstText.configure(font="TkTextFont")
        self.firstText.configure(foreground="black")
        self.firstText.configure(highlightbackground="#d9d9d9")
        self.firstText.configure(highlightcolor="black")
        self.firstText.configure(insertbackground="black")
        self.firstText.configure(selectbackground="#c4c4c4")
        self.firstText.configure(selectforeground="black")
        self.firstText.configure(width=164)
        self.firstText.configure(wrap=WORD)

        self.departmentText = Text(self.TFrame1)
        self.departmentText.place(relx=0.269, rely=0.292, relheight=0.054, relwidth=0.276)
        self.departmentText.configure(background="white")
        self.departmentText.configure(font="TkTextFont")
        self.departmentText.configure(foreground="black")
        self.departmentText.configure(highlightbackground="#d9d9d9")
        self.departmentText.configure(highlightcolor="black")
        self.departmentText.configure(insertbackground="black")
        self.departmentText.configure(selectbackground="#c4c4c4")
        self.departmentText.configure(selectforeground="black")
        self.departmentText.configure(width=164)
        self.departmentText.configure(wrap=WORD)

        self.lastText = Text(self.TFrame1)
        self.lastText.place(relx=0.269, rely=0.202, relheight=0.054, relwidth=0.276)
        self.lastText.configure(background="white")
        self.lastText.configure(font="TkTextFont")
        self.lastText.configure(foreground="black")
        self.lastText.configure(highlightbackground="#d9d9d9")
        self.lastText.configure(highlightcolor="black")
        self.lastText.configure(insertbackground="black")
        self.lastText.configure(selectbackground="#c4c4c4")
        self.lastText.configure(selectforeground="black")
        self.lastText.configure(width=164)
        self.lastText.configure(wrap=WORD)

        self.addButton = ttk.Button(self.TFrame1)
        self.addButton.place(relx=0.084, rely=0.539, height=25, width=76)
        self.addButton.configure(takefocus="")
        self.addButton.configure(text='''Add''')
        self.addButton.configure(command=self.add_comannd)

        self.deleteButton = ttk.Button(self.TFrame1 )
        self.deleteButton.place(relx=0.336, rely=0.539, height=25, width=76)
        self.deleteButton.configure(takefocus="")
        self.deleteButton.configure(text='''Delete''')
        self.deleteButton.configure(command=self.delete_command)

        self.updateButton = ttk.Button(self.TFrame1 )
        self.updateButton.place(relx=0.571, rely=0.539, height=25, width=76)
        self.updateButton.configure(takefocus="")
        self.updateButton.configure(text='''Update''')
        self.updateButton.configure(command=self.update_command)

        self.showButton = ttk.Button(self.TFrame1 )
        self.showButton.place(relx=0.79, rely=0.539, height=25, width=76)
        self.showButton.configure(takefocus="")
        self.showButton.configure(text='''Show''')
        self.showButton.configure(command=self.view_command)

        self.showListbox = Listbox(self.TFrame1)
        self.showListbox.place(relx=0.017, rely=0.607, relheight=0.342
                , relwidth=0.931)
        self.showListbox.configure(background="white")
        self.showListbox.configure(disabledforeground="#a3a3a3")
        self.showListbox.configure(font="TkFixedFont")
        self.showListbox.configure(foreground="#000000")
        self.showListbox.configure(highlightbackground="#d9d9d9")
        self.showListbox.configure(highlightcolor="black")
        self.showListbox.configure(justify=CENTER)
        self.showListbox.configure(selectbackground="#c4c4c4")
        self.showListbox.configure(selectforeground="black")
        self.showListbox.configure(width=554)

        self.Label6 = Label(self.TFrame1)
        self.Label6.place(relx=0.05, rely=0.022, height=31, width=114)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Register No.''')

        self.YearText = Text(self.TFrame1)
        self.YearText.place(relx=0.269, rely=0.382, relheight=0.054
                , relwidth=0.276)
        self.YearText.configure(background="white")
        self.YearText.configure(font="TkTextFont")
        self.YearText.configure(foreground="black")
        self.YearText.configure(highlightbackground="#d9d9d9")
        self.YearText.configure(highlightcolor="black")
        self.YearText.configure(insertbackground="black")
        self.YearText.configure(selectbackground="#c4c4c4")
        self.YearText.configure(selectforeground="black")
        self.YearText.configure(width=164)
        self.YearText.configure(wrap=WORD)

        self.RegisterText = Text(self.TFrame1)
        self.RegisterText.place(relx=0.269, rely=0.022, relheight=0.054
                , relwidth=0.276)
        self.RegisterText.configure(background="white")
        self.RegisterText.configure(font="TkTextFont")
        self.RegisterText.configure(foreground="black")
        self.RegisterText.configure(highlightbackground="#d9d9d9")
        self.RegisterText.configure(highlightcolor="black")
        self.RegisterText.configure(insertbackground="black")
        self.RegisterText.configure(selectbackground="#c4c4c4")
        self.RegisterText.configure(selectforeground="black")
        self.RegisterText.configure(width=164)
        self.RegisterText.configure(wrap=WORD)

     def __del__(self):
         conn.close()


if __name__ == '__main__':
    vp_start_gui()



