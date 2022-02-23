from msilib.schema import File
import tkinter as tk
import pandas as ps
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = ps.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = ps.read_csv("data/french_words.csv")
finally:
    words_to_learn = data.to_dict(orient="records")

current_card = {}
#------------------------------------------- FLIP CARD SETUP -------------------------------------------#

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)
#------------------------------------------- NEXT CARD SETUP -------------------------------------------#
def is_known():
    words_to_learn.remove(current_card)
    print(len(words_to_learn))
    next_card()
    data = ps.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global current_card
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    window.after(3000, func=flip_card)
#------------------------------------------- UI SETUP -------------------------------------------#  
window = tk.Tk()
window.title("Flashy")
window.config(padx=80, pady=15, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Courier", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Courier", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=check_image, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()

