from tkinter import *
import pandas as pd
import random as random

BACKGROUND_COLOR = "#B1DDC6"

# Part 1: Importing the data
# Importing the data from the csv file
df = pd.read_csv("data/french_words.csv")
to_learn = df.to_dict(orient="records")
current_card = {}
flip_timer = 0


def main():
  global flip_timer, current_card
  
  def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word,text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

  def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word,text=current_card["English"], fill="white")

  
  window = Tk()
  window.title("Flashy")
  window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
  
  flip_timer = window.after(3000, flip_card)

  #Images
  wrong_img = PhotoImage(file="images/wrong.png")
  right_img = PhotoImage(file="images/right.png")
  card_back_img = PhotoImage(file="images/card_back.png")
  card_front_img = PhotoImage(file="images/card_front.png")

  #Canvas
  canvas = Canvas(width=800,
                  height=526,
                  bg=BACKGROUND_COLOR,
                  highlightthickness=0)
  canvas_img = canvas.create_image(400, 263, image=card_front_img)
  canvas.grid(column=0, row=0, columnspan=2)
  language = canvas.create_text(400,
                                150,
                                text="French",
                                font=("Arial", 40, "italic"))
  word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

  #Buttons
  wrong_button = Button(image=wrong_img,
                        highlightbackground=BACKGROUND_COLOR,
                        highlightthickness=0,
                        command=next_card)
  wrong_button.grid(row=1, column=0)
  right_button = Button(image=right_img,
                        highlightthickness=0,
                        command=next_card)
  right_button.grid(row=1, column=1)

  next_card()
  
  window.mainloop()