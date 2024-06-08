# import necessary libraries
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from threading import Thread
from datetime import datetime
from time import sleep

# ===================================================== Colors =============================================
bg_color = "#ffffff"
color_1 = "#566FC6"
color_2 = "#ffffff"

mixer.init()

# ===================================================== Window =============================================
window = Tk()
window.title("")
window.geometry("400x150")
window.configure(bg=bg_color)

# ===================================================== Frames =============================================
frame_line = Frame(window, width=400, height=5, bg=color_1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=color_2)
frame_body.grid(row=1, column=0)

# ===================================================== Images =============================================
img = Image.open('alarm-clock-icon.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=12)

# ============================================= Labels and Controls ========================================
label_name = Label(frame_body, text= 'Alarm', height=1, font=('Ivy 18 bold'), bg=bg_color)
label_name.place(x=125, y=10)

label_hour = Label(frame_body, text= 'hour', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=color_1)
label_hour.place(x=126, y=40)

combo_hour = Combobox(frame_body, width=3, font=('arial 12'))
combo_hour['values'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
combo_hour.current(0)
combo_hour.place(x=130, y=58)

label_minutes = Label(frame_body, text= 'minutes', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=color_1)
label_minutes.place(x=180, y=40)

combo_minutes = Combobox(frame_body, width=3, font=('arial 12'))
combo_minutes['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
combo_minutes.current(0)
combo_minutes.place(x=184, y=58)

label_seconds = Label(frame_body, text= 'seconds', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=color_1)
label_seconds.place(x=234, y=40)

combo_seconds = Combobox(frame_body, width=3, font=('arial 12'))
combo_seconds['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
combo_seconds.current(0)
combo_seconds.place(x=238, y=58)

label_period = Label(frame_body, text= 'period', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=color_1)
label_period.place(x=288, y=40)

combo_period = Combobox(frame_body, width=3, font=('arial 11'))
combo_period['values'] = ("AM", "PM")
combo_period.current(0)
combo_period.place(x=292, y=58)

# ================================================== Alarm Sound ==============================================
def sound_alarm():
    mixer.music.load('alarm.wav')
    mixer.music.play()
    selected.set(0)

    radio_2 = Radiobutton(frame_body, font = ('arial 10 bold'), value = 2, text='Deactivate', bg = bg_color, command=deactivate_alarm, variable=selected)
    radio_2.place(x=187, y=95)

# ===================================================== Alarm =================================================
def alarm():
    while True:
        control = selected.get()

        alarm_hour = combo_hour.get()
        alarm_minute = combo_minutes.get()
        alarm_seconds = combo_seconds.get()
        alarm_period = str(combo_period.get()).upper()

        now = datetime.now()
        current_hour = now.strftime('%I')
        current_minutes = now.strftime('%M')
        current_seconds = now.strftime('%S')
        current_period = now.strftime('%p')

        if control == 1:
            if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_minute == current_minutes:
                        if alarm_seconds == current_seconds:
                            print("Time to take a break!")
                            sound_alarm()

        sleep(1)


# ================================================ Activate Alarm =============================================
def activate_alarm():
    t = Thread(target=alarm)
    t.start()


# =============================================== Deactivate Alarm ============================================
def deactivate_alarm():
    print("Deactivate alarm")
    mixer.music.stop()


# controls for activation / deactivation
selected = IntVar()

radio_1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text='Activate', bg=bg_color, command=activate_alarm, variable=selected)
radio_1.place(x=125, y=95)

# main window
window.mainloop()