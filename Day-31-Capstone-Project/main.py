from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ----------------------- UI Setup ------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_butt = Button(image=wrong_img, highlightthickness=0)
wrong_butt.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_butt = Button(image=right_img, highlightthickness=0)
right_butt.grid(column=1, row=1)

window.mainloop()
