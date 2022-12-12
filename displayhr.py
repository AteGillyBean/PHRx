from tkinter import *
root=Tk()
root.geometry("300x50")
root.title("Heart Rate")
label=Label(root)
label.pack(pady=20)
def update_hr():
    with open('/home/pi/Downloads/avg.txt', 'r') as v:
        avg=v.read()
    label.config(text="Heart Rate: " + avg + " BPM")
    root.after(100,update_hr)
    
update_hr()
root.mainloop()


