from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

#Label
timer_title = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_title.grid(column=1, row=0)

#Buttons
btn_start = Button(text='Start', highlightthickness=0)
btn_start.grid(column=0, row=2)
btn_reset = Button(text='Reset', highlightthickness=0)
btn_reset.grid(column=2, row=2)

#Checkmark
checkmark_label = Label(text='✓', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
checkmark_label.grid(column=1, row=3)

window.mainloop()