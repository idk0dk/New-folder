import tkinter as tk
from PIL import Image, ImageTk
import random

def pick_weighted_card(cards):
    weights = [1.0 / (card['score'] + 1) for card in cards]
    return random.choices(cards, weights=weights, k=1)[0]


# Hiragana flashcards
hiragana_cards = [
    {"kana": "あ", "romaji": "a", "score": 0},
    {"kana": "い", "romaji": "i", "score": 0},
    {"kana": "う", "romaji": "u", "score": 0},
    # etc.
]

class JapaneseLearnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Japanese Kana")
        self.root.geometry("600x500")  # Resize as needed

        # Load and set the background image
        
        # Background image
        self.bg_image = Image.open("1600w-D0NN5x65Bo8.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Foreground widgets (labels, buttons)
        self.show_button = tk.Button(root, text="Show New Kana", command=self.show_random_card, bg="#d8bfd8")
        self.show_button.place(relx=0.5, rely=0.7, anchor="center")

        self.reveal_button = tk.Button(root, text="Reveal Romaji", command=self.reveal_romaji, bg="#d8bfd8")
        self.reveal_button.place(relx=0.5, rely=0.75, anchor="center")


        self.show_button = tk.Button(root, text="Show New Kana", command=self.show_random_card)
        self.show_button.place(relx=0.5, rely=0.7, anchor="center")

        self.reveal_button = tk.Button(root, text="Reveal Romaji", command=self.reveal_romaji)
        self.reveal_button.place(relx=0.5, rely=0.75, anchor="center")
        
        self.kana_label = tk.Label(root, text="", font=("Helvetica", 100), bg="#ffe4e1")
        self.kana_label.place(relx=0.5, rely=0.3, anchor="center")
        
        self.right_button = tk.Button(root, text="Got it Right ✅", command=self.mark_correct)
        self.right_button.place(relx=0.4, rely=0.85, anchor="center")
        self.wrong_button = tk.Button(root, text="Oops, Wrong ❌", command=self.mark_wrong)
        self.wrong_button.place(relx=0.6, rely=0.85, anchor="center")



    def show_random_card(self):
        self.current_card = pick_weighted_card(hiragana_cards)
        self.kana_label.config(text=self.current_card["kana"])
        self.romaji_label.config(text="")


    def reveal_romaji(self):
        if self.current_card:
            self.romaji_label.config(text=self.current_card["romaji"])
            
    def mark_correct(self):
        self.current_card["score"] += 1
        self.show_random_card()

    def mark_wrong(self):
        self.current_card["score"] = max(self.current_card["score"] - 1, 0)
        self.show_random_card()


# Start app
root = tk.Tk()
app = JapaneseLearnerApp(root)
root.mainloop()
