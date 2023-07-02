from tkinter import *

import calendar

def showCalender():
    gui = Tk()
    gui.config(background='blue')
    gui.title("CALENDAR")
    gui.geometry("600x700")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Helvetica 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()


if __name__=='__main__':
    new = Tk()
    new.config(background='blue')
    new.title("Calendar")
    new.geometry("250x140")
    cal = Label(new, text="Calender", bg='grey', font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calender',
                    fg='Black', bg='Blue', command=showCalender)

cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
button.grid(row=4, column=1)
Exit.grid(row=6, column=1)
new.mainloop()