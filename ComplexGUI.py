import tkinter as tk
from tkinter import filedialog, messagebox, Menu, simpledialog, Label
from tkinter.filedialog import asksaveasfile
import os
import sys
import time
def save():
#     files=[('Text Document', '*.txt')]
#     filesave=asksaveasfile(filetypes=files, defaultextension=files)
    answer4 = messagebox.askyesno(title = "Confirmation", message = "Are you sure you want to save? You will not be able to add any new data to this file.")
    if answer4==True:
        x=simpledialog.askstring(title='Data Filename', prompt='Enter your filename: ')
        with open('/home/pi/Downloads/log.txt', 'r') as s:
            os.rename('/home/pi/Downloads/log.txt', '{}.txt'.format(x))
def open_file():
    fileopen=filedialog.askopenfile()
def start():
    answer5 = messagebox.askyesno(title = "Confirmation", message = "Are you sure you want to restart? Any unsaved data will be lost.")
    if answer5==True:
        os.popen('python /home/pi/Downloads/datatest.py')
        with open('/home/pi/Downloads/log.txt', 'w') as f:
            pass
        starttime=time.time()
        with open('/home/pi/Downloads/start.txt', 'w') as q:
            q.write(str(starttime))
        os.popen('python /home/pi/Downloads/PlotTest.py')
def resume():
    os.popen('python /home/pi/Downloads/datatest.py')
    os.popen('pkill -f /home/pi/Downloads/PlotTest.py')
    os.popen('python /home/pi/Downloads/PlotTest.py')
# def plotdata():
#     os.popen('python /home/pi/Downloads/PlotTest.py')
def stopprogram():
    os.popen('pkill -f /home/pi/Downloads/datatest.py')
def exitfile():
    answer3 = messagebox.askyesno(title = "Confirmation", message = "Are you sure you want to clear your data file? Any unsaved data will be lost.")
    if answer3==True:
        os.popen('pkill -f /home/pi/Downloads/datatest.py')
        os.popen('pkill -f /home/pi/Downloads/PlotTest.py')
def exitcommand():
    answer2 = messagebox.askyesno(title = "Confirmation", message = "Are you sure you want to quit? Any unsaved data will be lost.")
    if answer2==True:
        os.popen('pkill -f /home/pi/Downloads/datatest.py')
        os.popen('pkill -f /home/pi/Downloads/PlotTest.py')
        os.popen('pkill -f /home/pi/Downloads/displayhr.py')
        os.popen('pkill -f /home/pi/Downloads/Endplot.py')
        root.destroy()
def display_beat():
    os.popen('python /home/pi/Downloads/displayhr.py')
def plot_final():
    os.popen('python /home/pi/Downloads/Endplot.py')
# def restart():
#     answer1 = messagebox.askyesno(title = "Confirmation", message = "Are you sure you want to quit? Any unsaved data will be lost.")
#     if answer1==True:
#         os.popen('pkill -f /home/pi/Downloads/datatest.py')
#         os.popen('pkill -f /home/pi/Downloads/PlotTest.py')
#         os.popen('python /home/pi/Downloads/datatest.py')
#         os.popen('python /home/pi/Downloads/PlotTest.py')

    
root = tk.Tk()
root.title("PHRx Program")
root.geometry("500x500")

menubar=Menu(root)
root.config(menu=menubar)

file_menu=Menu(menubar,tearoff=0)
file_menu.add_command(label='Save',command=save)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exitfile)

menubar.add_cascade(label='File',menu=file_menu)
# with open('/home/pi/Downloads/avg.txt', 'r') as v:
#     avg=v.read()
# label=Label(root, text=avg)
# label.pack()
# def update():
#     
#     with open('/home/pi/Downloads/avg.txt', 'r') as v:
#         avg=v.read()
#     root.after(1000, update)
# update()


button1 = tk.Button(root,text="Start New Data Collection",command=start, width = 20)
# button2 = tk.Button(root,text="Clear Data",command=exitfile, width = 20)
button5 = tk.Button(root,text="Resume Collection",command=resume, width = 20)
button3 = tk.Button(root,text="Pause Collection",command=stopprogram, width = 20)
button6 = tk.Button(root,text="Display Heart Rate",command=display_beat, width = 20)
button7 = tk.Button(root,text="Plot All Data",command=plot_final, width = 20)
button4 = tk.Button(root,text="Exit to Desktop",command=exitcommand, width = 20)
# button6 = tk.Button(root,text="Restart Data Collection",command=restart,width=20)
# button7 = tk.Button(root,text="Save",command=save,width=20)

button1.pack()
button5.pack()
button3.pack()
# button2.pack()
button6.pack()
button7.pack()
button4.pack()
# button6.pack()
# button7.pack()

root.mainloop()


