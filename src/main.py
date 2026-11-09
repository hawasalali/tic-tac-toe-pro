import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("900x1000")

PLAYER = "X"
buttons = []

x_score = 0
o_score = 0

x_plays = 0
o_plays = 0


def change_player():
    global PLAYER

    if PLAYER == "X":
        PLAYER = "O"
    else:
        PLAYER = "X"

    player_label.config(text=f"Current Player: {PLAYER}")


def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")


def reset_game():
    global PLAYER

    PLAYER = "X"
    player_label.config(text="Current Player: X")

    for btn in buttons:
        btn.config(
            text="-",
            bg="#34F1FE",
            fg="black",
            state="normal"
        )


def reset_score():
    global x_score, o_score
    global x_plays, o_plays

    x_score = 0
    o_score = 0

    x_plays = 0
    o_plays = 0

    messagebox.showinfo(
        "Reset",
        "All scores reset!"
    )


def show_score():
    messagebox.showinfo(
        "Score",
        f"X Wins: {x_score}\n\nO Wins: {o_score}"
    )


def show_plays():
    messagebox.showinfo(
        "Plays",
        f"X gespielt: {x_plays} mal\n\nO gespielt: {o_plays} mal"
    )


def check_win():
    global x_score, o_score

    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in combinations:

        a, b, c = combo

        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] and buttons[a]["text"] != "-":

            winner = buttons[a]["text"]

            buttons[a].config(bg="yellow")
            buttons[b].config(bg="yellow")
            buttons[c].config(bg="yellow")

            if winner == "X":
                x_score += 1
            else:
                o_score += 1

            messagebox.showinfo(
                "Game Over",
                f"Player {winner} wins!"
            )

            disable_buttons()
            return True

    return False


def check_tie():

    if all(btn["text"] != "-" for btn in buttons):

        messagebox.showinfo(
            "Game Over",
            "Tie Game!"
        )

        disable_buttons()
        return True

    return False


def play(btn):
    global PLAYER
    global x_plays, o_plays

    if btn["text"] != "-":
        return

    if PLAYER == "X":

        x_plays += 1

        btn.config(
            text="X",
            bg="red",
            fg="black"
        )

    else:

        o_plays += 1

        btn.config(
            text="O",
            bg="green",
            fg="black"
        )

    if check_win():
        return

    if check_tie():
        return

    change_player()


for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(3):
    root.grid_columnconfigure(j, weight=1)

for row in range(3):
    for col in range(3):

        btn = tk.Button(
            root,
            text="-",
            font=("Arial", 60, "bold"),
            bg="#34F1FE"
        )

        btn.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=2,
            pady=2
        )

        btn.config(command=lambda b=btn: play(b))

        buttons.append(btn)


reset_button = tk.Button(
    root,
    text="RESET GAME",
    font=("Arial", 18, "bold"),
    bg="orange",
    command=reset_game
)

reset_button.grid(
    row=3,
    column=0,
    sticky="nsew",
    padx=2,
    pady=2
)


score_button = tk.Button(
    root,
    text="SHOW SCORE",
    font=("Arial", 18, "bold"),
    bg="lightgreen",
    command=show_score
)

score_button.grid(
    row=3,
    column=1,
    sticky="nsew",
    padx=2,
    pady=2
)


plays_button = tk.Button(
    root,
    text="SHOW PLAYS",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    command=show_plays
)

plays_button.grid(
    row=3,
    column=2,
    sticky="nsew",
    padx=2,
    pady=2
)


player_label = tk.Label(
    root,
    text="Current Player: X",
    font=("Arial", 24, "bold")
)

player_label.grid(
    row=4,
    column=0,
    columnspan=3,
    pady=10
)


reset_score_button = tk.Button(
    root,
    text="RESET SCORE",
    font=("Arial", 18, "bold"),
    bg="pink",
    command=reset_score
)

reset_score_button.grid(
    row=5,
    column=0,
    columnspan=3,
    sticky="nsew",
    padx=2,
    pady=2
)

root.mainloop()