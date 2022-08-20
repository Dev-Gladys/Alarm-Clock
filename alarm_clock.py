import datetime
from tkinter import messagebox
from tkinter import *
from time import *
import threading
from playsound import playsound


window =Tk()
window.geometry('600x500')
window.title("Alarm Clock")
window.config(padx=100, pady=50, bg ="blue")
canvas= Canvas(width=300, height =300, bg="white", highlightthickness=0)
clock_image = PhotoImage(file="C:\\Users\\glady\\PycharmProjects\\GithubProjects\\clock.png")
canvas.create_image(150, 110, image= clock_image)
timer_text=canvas.create_text(150,210, text="00:00:00", fill="black", font=("Arial",30,"bold"))
canvas.grid(column=1, row=1)



def update():
    current_time = strftime("%I:%M:%S %p")
    canvas.itemconfig(timer_text,  text=current_time)
    window.after(1000,update)


def set_alarm():
    hr = hour.get()
    mins= min.get()
    if hr == "" or mins == "":
        messagebox.showerror("Error!" ,message="Enter a Valid Time")
    else:
        while True:
            if (int(hr) == datetime.datetime.now().hour and int(mins)==datetime.datetime.now().minute):
                playsound("C:\\Users\\glady\\PycharmProjects\\GithubProjects\\alarm-sound.wav")
                messagebox.showinfo("Its Time!" ,message="Alarm Ringing")
                break


set_alarm_label=Label(window, text = 'Set Alarm',font=('calibre',13, 'bold'), bg="blue")
set_alarm_label.place(x=0, y=310)

hour= Entry(window, width=3, font=('calibre',10,'normal'))
hour.place(x=100, y=310)
hour_label=Label(window, text = 'Hr',font=('calibre',10, 'bold'), bg="blue")
hour_label.place(x=100, y=330)

min= Entry(window, width=3, font=('calibre',10,'normal'))
min.place(x=150, y=310)
mins_label=Label(window, text = 'Mins', font=('calibre',10, 'bold'),bg="blue")
mins_label.place(x=148, y=330)

set_alarmBtn= Button(window, text="Set Alarm",fg="white", activebackground="blue",font=("Arial",15, "bold"),
                     bg="blue",width=22, command=set_alarm).place(x=10, y=370)


threading.Thread(target=update).start()

window.mainloop()



