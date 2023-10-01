import tkinter as tk
import random
# Functions 
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def play_rock():
    play_round("Rock")

def play_paper():
    play_round("Paper")

def play_scissors():
    play_round("Scissors")

def play_round(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")
     
    # when user chioice and cmputer coice will be same 
    if user_choice == computer_choice:
        result_label.config(text=result_label.cget("text") + "\n Game Draw!")
    
    # for user wining circumstances
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text=result_label.cget("text") + "\nYou win!")
    # for Computer win circumstances
    else:
        computer_score += 1
        result_label.config(text=result_label.cget("text") + "\nComputer wins!")

    update_score_labels()

def update_score_labels():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score_labels()
    result_label.config(text="Make your choice below!")

def exit_game():
    window.destroy()

user_score = 0
computer_score = 0

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("500x350")

# Labels 
result_label = tk.Label(window, text="Make your choice below!", font=("Helvetica", 16))
result_label.pack()

user_score_label = tk.Label(window, text="Your Score: 0", font=("Helvetica", 12))
user_score_label.pack()
computer_score_label = tk.Label(window, text="Computer Score: 0", font=("Helvetica", 12))
computer_score_label.pack()


# Buttons 
rock_button = tk.Button(window, text="Rock", command=play_rock)
paper_button = tk.Button(window, text="Paper", command=play_paper)
scissors_button = tk.Button(window, text="Scissors", command=play_scissors)

rock_button.pack()
paper_button.pack()
scissors_button.pack()

reset_button = tk.Button(window, text="Play Again", command=reset_game)
exit_button = tk.Button(window, text="Exit Game", command=exit_game)

reset_button.pack()
exit_button.pack()

window.mainloop()
 