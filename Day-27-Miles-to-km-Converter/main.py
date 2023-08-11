import tkinter

def mile_to_km():
    result = float(miles.get()) * 1.609
    result_label.config(text=result)

window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

miles = tkinter.Entry(width=7)
miles.grid(column=1, row=0)

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)
    
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

my_button = tkinter.Button(text="Calculate", command=mile_to_km)
my_button.grid(column=1, row=2)

window.mainloop()
