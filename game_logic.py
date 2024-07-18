import random


class GameLogic:
    def __init__(self):
        self.user1 = False
        self.user2 = False
        self.count = 9
        self.user_name = ""
        self.buttons = ["" for _ in range(9)]
        self.game_on = True
        self.info_label = None

    def determine_first_user(self, info_label):  # function for determine who starts first
        self.info_label = info_label
        user_numb = random.randint(1, 2)
        if user_numb == 1:
            self.user1 = True
            self.user_name = "Player 1 starts"
        else:
            self.user2 = True
            self.user_name = "Player 2 starts"
        self.info_label.configure(text=self.user_name)

    def game_status_check(self):  # checks if the game ends or goes on
        for player in ["X", "O"]:
            if ((self.buttons[0] == self.buttons[1] == self.buttons[2] == player) or
                    (self.buttons[3] == self.buttons[4] == self.buttons[5] == player) or
                    (self.buttons[6] == self.buttons[7] == self.buttons[8] == player) or
                    (self.buttons[0] == self.buttons[3] == self.buttons[6] == player) or
                    (self.buttons[1] == self.buttons[4] == self.buttons[7] == player) or
                    (self.buttons[2] == self.buttons[5] == self.buttons[8] == player) or
                    (self.buttons[0] == self.buttons[4] == self.buttons[8] == player) or
                    (self.buttons[2] == self.buttons[4] == self.buttons[6] == player)):
                user = "Player1" if player == "X" else "Player2"
                self.end_game(f"{user} won the game")
                return
            if self.count == 0:
                self.end_game("Draw")

    def end_game(self, game_message):  # To end the game writes final message and sets flag for ending game
        self.info_label.configure(text=f"{game_message}")
        self.game_on = False

    def user_move(self, but_id, but_sel, info_label):  # main func. for playing game. writes user text to checked button
        self.info_label = info_label
        if self.buttons[but_id - 1] == "" and self.count > 0 and self.game_on:
            if self.user1:
                user_text = "X"
                self.user_name = "USER 2 TURN"
                self.user1 = False
                self.user2 = True
            else:
                user_text = "O"
                self.user_name = "USER 1 TURN"
                self.user1 = True
                self.user2 = False
            self.buttons[but_id - 1] = user_text
            but_sel.configure(text=user_text, )
            self.info_label.configure(text=self.user_name)
            self.count -= 1
            self.game_status_check()
