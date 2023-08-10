import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=300, height=200)

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

def calculate():
    result = float(miles.get()) * 1.609
    result_label.config(text=result)
    
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

my_button = tkinter.Button(text="Calculate", command=calculate)
my_button.grid(column=1, row=2)

miles = tkinter.Entry(width=10)
miles.grid(column=1, row=0)

window.mainloop()
