# importing modules
from tkinter import *
from pandas import *
import random


# importing the word list, transforming, and defining initial variables
language = "French"

# importing the word list
try:
    words_df = read_csv("words_to_learn.csv")
except FileNotFoundError:
    words_df = read_csv("data/french_words.csv")

words_dict = words_df.to_dict()

lang_dict = words_dict[language]

after_id = ""

english_shown = False


# functions 1
# generates a random key from the dictionary
def generate_key():
    rand_key = random.choice(list(lang_dict.keys()))
    return rand_key


key = generate_key()
word = ""

# gui setup
BACKGROUND_COLOR = "#B1DDC6"

font = "Arial"
language_size = 40
word_size = 60
language_style = "italic"
word_style = "bold"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# functions 2
# generate the next word to display
def generate_new_word():
    global key
    global word
    key = generate_key()
    word = lang_dict[key]
    return word

# more gui setup
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card = canvas.create_image(400, 263, image=card_front)
canvas_language_text = canvas.create_text(400, 150, text=language, font=(font, language_size, language_style))
canvas_word_text = canvas.create_text(400, 263, text=word, font=(font, word_size, word_style))
canvas.grid(column=0, columnspan=2, row=0)


# functions 3
# flip the card and show the English translation
def show_english():
    global word
    global english_shown
    english_shown = True
    temp_language = "English"
    temp_lang_dict = words_dict[temp_language]
    word = temp_lang_dict[key]
    canvas.itemconfigure(canvas_card, image=card_back)
    canvas.itemconfigure(canvas_language_text, text=temp_language, fill="white")
    canvas.itemconfigure(canvas_word_text, text=word, fill="white")


# update the screen to show the new word and correct colors
def update_screen():
    global after_id
    global word
    global english_shown
    global words_df
    global words_dict
    global lang_dict
    if after_id != "":
        window.after_cancel(after_id)
    if english_shown == False:
        words_df.drop(key, inplace=True)
        words_dict = words_df.to_dict()
        lang_dict = words_dict[language]
    word = generate_new_word()
    canvas.itemconfigure(canvas_card, image=card_front)
    canvas.itemconfigure(canvas_language_text, text=language, fill="black")
    canvas.itemconfigure(canvas_word_text, text=word, fill="black")
    english_shown = False
    after_id = window.after(3000, show_english)

# initial screen update
update_screen()

# more gui setup - the buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=show_english)
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=update_screen)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

mainloop()

# after closing the gui, write the updated list to a csv
words_df.to_csv("words_to_learn.csv", index=False)
