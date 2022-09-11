import numpy as np
import pandas as pd

# Creating empty series
ser = pd.Series()
  
print(ser)
  
# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
  
ser = pd.Series(data)
print(ser)

import datetime
import time
#from playsound import playsound
from tkinter import *

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime(f'%H:%M:%S')
        date = current_time.strftime(f'%d/%m/%Y')
        print(f'Current time is {date} {now}')

        if now == set_alarm_timer:
            print(f'Time to wake up!')
            #playsound('Audio.mp3')

def actual_time():
    set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
    alarm(set_alarm_timer)

clock = Tk()
clock.title('My Alarm Clock')
clock.geometry('350x180')
time_format = Label(clock, text = 'Enter time in 24 hour format',
                    fg = 'orange', bg = 'purple', font = 'Monaco').place(x = 60, y = 120)
addTime = Label(clock, text = 'Hour        Min          Sec', font = ('Helvetica', 12)).place(x = 135, y = 10)
setYourAlarm = Label(clock, text = 'When to wake you up?', fg = 'pink', relief = 'sunken',
                font = ('Helvetica', 10, 'bold')).place(x = 10, y = 35)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable = hour, bg = 'pink', width = 10).place(x = 133, y = 30)
minTime = Entry(clock, textvariable = min, bg = 'pink', width = 10).place(x = 183, y = 30)
secTime = Entry(clock, textvariable = sec, bg = 'pink', width = 10).place(x = 233, y = 30)

submit = Button(clock, text = 'Set Alarm', fg = 'skyblue', font = ('Helvetica', 13, 'bold'),
                relief = 'raised', width = 10, command = actual_time).place(x = 135, y = 70)

clock.mainloop()