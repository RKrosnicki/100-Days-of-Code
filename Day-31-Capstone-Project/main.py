from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = "Ariel", 60, "bold"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------------- READ DATA FILE ------------------

try:
    data_file = pd.read_csv("data/to_learn.csv")
    data = data_file.to_dict(orient='records')
except (FileNotFoundError, pd.errors.EmptyDataError):
    data_file = pd.read_csv("data/french_words.csv")
    data = data_file.to_dict(orient='records')

# ---------------------- MECHANISM -------------------------

def next_card():
    global current_card, flip_timer, data
    print(len(data))
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=card_front_img)
    try:
        current_card = random.choice(data)
    except IndexError:
        messagebox.showinfo(title="You've done it!", message="Congratulations, you've learned them all!")
        temp_file = pd.read_csv("data/french_words.csv")
        data = temp_file.to_dict(orient='records')

    canvas.itemconfig(lang_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, show_answer)

def show_answer():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(lang_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')

def save_progress(data_list):
    df = pd.DataFrame(data_list)
    df.to_csv("data/to_learn.csv", index=False)

def right_button():
    next_card()
    data.remove(current_card)
    save_progress(data)

# ----------------------- UI Setup ------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, show_answer)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
lang_text = canvas.create_text(400, 150, text='', font=FONT_LANG)
word_text = canvas.create_text(400, 263, text='', font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_butt = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_butt.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_butt = Button(image=right_img, highlightthickness=0, bd=0, command=right_button)
right_butt.grid(column=1, row=1)

next_card()

window.mainloop()
