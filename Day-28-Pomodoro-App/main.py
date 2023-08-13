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
reps = 0
break_time = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global break_time
    global timer
    global count
    canvas.itemconfig(timer_text, text="00:00")
    count = 0
    window.after_cancel(timer)
    reps = 0
    break_time = False
    start_button.config(text="start")
    title_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global break_time

    if not break_time:
        title_label.config(text="WORKING", fg=GREEN)
        break_time = 1
        count_down(WORK_MIN * 60)
    else:
        reps += 1
        if break_time and reps > 0 and reps % 4 == 0:
            title_label.config(text="RESTING LONGER", fg=RED)
            reps = 0
            break_time = False
            count_down(LONG_BREAK_MIN * 60)
        else:
            break_time = False
            title_label.config(text="RESTING", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    if break_time:
        start_button.config(text="start break")
    else:
        start_button.config(text="start work")

    mins = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")

    if count > 0:
        timer = window.after(10, count_down, count-1)
    elif count == 0:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
    checkmarks.config(text=reps * "✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="start", width=10, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", width=10, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text=" ", fg=GREEN, bg=YELLOW, font=(50))
checkmarks.grid(column=1, row=3)

window.mainloop()
