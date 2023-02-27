from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    timer_title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text='')

    # timer to zero
    # title to timer
    # reset checkmarks

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    print(f"Reps: {reps}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep
    if reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text='Work', fg=GREEN)
    # # if it's the 8th rep:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text='Break', fg=RED)
    # # if it's the 2nd/4th/6th rep:
    elif reps % 2 == 0 and reps % 8 != 0:
        count_down(short_break_sec)
        timer_title.config(text='Break', fg=PINK)

    # count_down(5)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    #     count_sec = '00'

    canvas.itemconfig(timer_text, text=f"{count_min}:{'{:02d}'.format(count_sec)}")
    # print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        # reps += 1
        # print(f"{reps}")
        # print('After countdown')
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark +='✓'
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)



#Label
timer_title = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_title.grid(column=1, row=0)

#Buttons
btn_start = Button(text='Start', highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
btn_reset.grid(column=2, row=2)

#Checkmark
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
checkmark_label.grid(column=1, row=3)

window.mainloop()