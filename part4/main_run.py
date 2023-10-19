from tkinter import *
import pandas as pd
import random as random

BACKGROUND_COLOR = "#B1DDC6"


def main():

  # Part 1: Importing the data
  # Importing the data from the csv file
  df = pd.read_csv("data/french_words.csv")
  df_dict = df.to_dict(orient="records")

  def random_word():
    random_word = df_dict[random.randint(0, len(df_dict) - 1)]
    print(random_word)
    french_string = list(random_word.keys())[0]
    french_word = random_word["French"]
    # Displaying the title language
    canvas.itemconfig(language, text=french_string)
    # Displaying the word language
    canvas.itemconfig(word,text=french_word)

  window = Tk()
  window.title("Flashy")
  window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
  canvas.create_image(400, 263, image=card_front_img)
  canvas.grid(column=0, row=0, columnspan=2)
  language = canvas.create_text(400,
                                150,
                                text="French",
                                font=("Arial", 40, "italic"))
  word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

  random_word()
  #Buttons
  wrong_button = Button(image=wrong_img,
                        highlightbackground=BACKGROUND_COLOR,
                        highlightthickness=0,
                        command=random_word)
  wrong_button.grid(row=1, column=0)
  right_button = Button(image=right_img,
                        highlightthickness=0,
                        command=random_word)
  right_button.grid(row=1, column=1)

  mainloop()
