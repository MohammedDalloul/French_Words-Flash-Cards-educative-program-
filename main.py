from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict_list = {}

try:
    words_file = pandas.read_csv("data/words to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict_list = original_data.to_dict(orient="records")
else:
    data_dict_list = words_file.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card
    global timer_flipper
    window.after_cancel(timer_flipper)
    current_card = random.choice(data_dict_list)
    canvas.itemconfig(canvas_image, image=frontg)
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    timer_flipper = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=frontg2)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


def word_remove():
    global current_card
    data_dict_list.remove(current_card)
    data = pandas.DataFrame(data_dict_list)
    data.to_csv("data/words to learn.csv", index=False)

    next_card()


window = Tk()
window.title("Mohammed flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer_flipper = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

frontg = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=frontg)
frontg2 = PhotoImage(file="images/card_back.png")

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=word_remove)
right_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

card_language = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "normal"))
card_word = canvas.create_text(400, 260, text="Word", font=("Ariel", 40, "bold"))

next_card()

canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()
