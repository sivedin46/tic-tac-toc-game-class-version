import tkinter as tk
from game_logic import GameLogic


class TicTocGui:  # Creates game board
    def __init__(self):
        self.game = GameLogic()
        self.lb = tk.Tk()
        self.lb.title("Tic Toc Game")
        self.lb.configure(bg="salmon3")
        self.lb.geometry("550x600+10+10")
        self.lb.resizable(False, False)
        self.i = tk.PhotoImage(width=1, height=1)
        self.info_label = tk.Label(text="", bg="salmon3", fg="salmon4", font=('arial', 20, 'bold'))
        self.info_label.place(x=10 + 10, y=550, width=500, height=50)
        self.button_size = 170
        self.padding = 10
        self.button_count = 1
        self.create_button()
        self.game.determine_first_user(self.info_label)
        self.lb.mainloop()

    def create_button(self):  # create 3*3 game board with buttons. also calls user_move to write user text
        for row in range(3):
            for col in range(3):
                button_id = f"{self.button_count}"
                button = tk.Button(
                    self.lb,
                    relief="flat",
                    borderwidth=0,
                    bg="salmon2",
                    activebackground="salmon2",
                    font=('arial', 80, 'bold'),
                    image=self.i,
                    compound='bottom',
                    anchor="center",
                    fg="salmon4",

                )
                button.config(
                    command=lambda b=button, b_id=int(button_id): self.game.user_move(b_id, b, self.info_label))
                button.place(x=col * (self.button_size + self.padding) + self.padding,
                             y=row * (self.button_size + self.padding) + self.padding,
                             width=self.button_size, height=self.button_size)
                self.button_count += 1
