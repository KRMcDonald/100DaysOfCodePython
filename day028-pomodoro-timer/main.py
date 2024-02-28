from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Roboto"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 4

rep_counter = 0
rep_time_list = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN,
                 LONG_BREAK_MIN]

timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmark_string
    global rep_counter
    global timer_text
    global title_text
    checkmark_string = ""
    rep_counter = 0
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(title_text, text=timer_title_dict[rep_counter], fill=title_fg_color_dict[rep_counter])
    canvas.itemconfig(checkmark_counter, text=checkmark_string)
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(rep_time_list[rep_counter] * 60)


def add_checkmark():
    global checkmark_string
    global checkmark
    if rep_counter % 2 == 1:
        checkmark_string += checkmark



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global rep_counter
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        ct_min = str(math.floor(count / 60))
        ct_sec = str(count % 60)
        if len(ct_min) < 2:
            ct_min = "0" + ct_min
        if len(ct_sec) < 2:
            ct_sec = "0" + ct_sec
        time_string = ct_min + ":" + ct_sec
        canvas.itemconfig(timer_text, text=time_string)
        canvas.itemconfig(title_text, text=timer_title_dict[rep_counter], fill=title_fg_color_dict[rep_counter])
    elif count == 0:
        print(f"before raise {rep_counter}")
        add_checkmark()
        canvas.itemconfig(checkmark_counter, text=checkmark_string)
        print(f"checkmark string {checkmark_string}")
        rep_counter += 1
        print(f"after raise {rep_counter}")
        if rep_counter <= 7:
            start_timer()
        else:
            canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=350, bg=YELLOW, highlightthickness=0)

# title text
title_fg_color_dict = {0: GREEN, 1: PINK, 2: GREEN, 3: PINK, 4: GREEN, 5: PINK, 6: GREEN, 7: RED}
timer_title_dict= {0: "Work", 1: "Short Break", 2: "Work", 3: "Short Break", 4: "Work", 5: "Short Break",6: "Work", 7: "Long Break"}
title_text = canvas.create_text(150, 25, text=timer_title_dict[rep_counter], font=(FONT_NAME, 30, "bold"), fill=title_fg_color_dict[rep_counter])

# tomato
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 175, image=tomato_img)

# countdown
timer_text = canvas.create_text(150, 175, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=0)

# buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

start.grid(column=0, row=3)
reset.grid(column=2, row=3)

# checkmarks
checkmark = "✔ "
checkmark_string = ""

checkmark_counter = canvas.create_text(150, 320, text=checkmark_string, fill=GREEN, font=(FONT_NAME, 30, "normal"))
canvas.grid(column=1, row=2)


window.mainloop()
