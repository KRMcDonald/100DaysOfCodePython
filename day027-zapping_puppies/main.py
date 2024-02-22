from tkinter import *

window = Tk()
window.title("Test of Doom")
window.minsize(1200, 500)
window["bg"] = "black"

puppy_counter = 0
# print(f"original count: {puppy_counter}")
feels = "xyz"
inputx = Entry(width=100)
lab5 = Label(text=f"PUPPIES FRIED: {puppy_counter}", font=("Consolas", 24, "bold"), bg="black", fg="red")


def quitx():
    window.destroy()


def sick_bastard():
    global puppy_counter
    global lab5
    puppy_counter += 1
    # print(f"sick bastard count 1: {puppy_counter}")
    if puppy_counter == 2:
        lab7 = Label(text="ANOTHER ONE BITES THE DUST. ZZZING.", fg="yellow", bg="black", font=("Consolas", 24, "bold"))
        lab7.pack()
    lab5["text"] = f"PUPPIES FRIED: {puppy_counter}"
    lab5.pack()


def clicked():
    global puppy_counter
    # print(f"clicked count: {puppy_counter}")
    if puppy_counter == 0:
        puppy_counter += 1
        # print(f"clicked count if: {puppy_counter}")
        lab["fg"] = "yellow"
        lab["text"] = "OH $#@% YOU CLICKED IT YOU ELECTROCUTED A PUPPY YOU MONSTER"
        lab.pack()
        butt["text"] = "lolpwned"
        butt.pack()
        lab2 = Label(text="HOW DO YOU FEEL ABOUT YOURSELF NOW?", font=("Consolas", 24, "bold"), bg="teal", fg="black")
        lab2.pack()
        butt2 = Button(text="Enter", font=("Consolas", 12, "bold"), bg="teal", fg="black", command=clicked2)
        inputx.pack()
        butt2.pack()


def clicked2():
    global puppy_counter
    global lab5
    lab3 = Label(text=f"SO YOU FEEL {inputx.get().upper()}, DO YOU?", font=("Consolas", 24, "bold"), bg="black",
                 fg="yellow")
    lab3.pack()
    lab4 = Label(text="WELL TOO BAD. YOU JUST COULDN'T FOLLOW INSTRUCTIONS.", font=("Consolas", 24, "bold"),
                 bg="black", fg="yellow")
    lab4.pack()
    lab5["text"] = f"PUPPIES FRIED: {puppy_counter}"
    lab5.pack()
    lab6 = Label(text="TASTES LIKE BBQ CHICKEN.", font=("Consolas", 12, "bold"), bg="black", fg="orange")
    lab6.pack()
    lab7 = Label(text="pssst. are you a sick bastard? yeah, you all are.", font=("Consolas", 12, "normal"),
                 bg="black", fg="teal")
    butt4 = Button(text="yes", font=("Consolas", 12, "bold"), bg="teal", fg="black", command=sick_bastard)
    butt4.pack(side="bottom")
    lab7.pack(side="bottom")


# start  main program code
lab = Label(text="DANGER: DO NOT CLICK BUTTON", font=("Consolas", 24, "bold"), fg="red", bg="black")
lab.pack()

butt = Button(text="I will give you your dreams. For a price...", font=("Consolas", 12, "bold"), bg="orange",
              command=clicked)
butt.pack()

butt3 = Button(text="Quit (wut u scared?)", font=("Consolas", 12, "normal"), bg="red", command=quitx)
butt3.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

mainloop()
