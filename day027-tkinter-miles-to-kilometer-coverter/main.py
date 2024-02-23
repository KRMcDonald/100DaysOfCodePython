from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

convert_to_label = Label(text="is equal to")
convert_to_label.grid(column=0, row=1)

km_results = Label(text="0")
km_results.grid(column=1, row=1)


def calculate():
    global km_results
    m = float(miles_input.get())
    km = round(float(m * 1.609344), 2)
    km_results["text"] = km


km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=3)

mainloop()
