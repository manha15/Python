from tkinter import*
import random
import tkinter.font as font

computer_score = 0
player_score = 0

options = [('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score
    global player_score

    computer_score += 1
    winner_label.config(text="Computer Won!!")

    computer_score_label.config(text='Computer Score: ' + str(computer_score))
    player_score_label.config(text='Player Score: ' + str(player_score))


def player_wins():
    global player_score
    global computer_score

    player_score += 1
    winner_label.config(text='Player Won!!')

    computer_score_label.config(text='Computer Score: ' + str(computer_score))
    player_score_label.config(text='Player Score: ' + str(player_score))

def tie():
    global player_score
    global computer_score

    winner_label.config(text="TIE!!!")

    computer_score_label.config(text='Computer Score: ' + str(computer_score))
    player_score_label.config(text='Player Score: ' + str(player_score))

def get_computer_choice():
    return random.choice(options)

window = Tk()
window.title("Rock Paper Scissor Game")

app_font = font.Font(size =  12)

game_title = Label(window, text="Rock Paper Scissors", font= font.Font(size=20), fg="grey")
game_title.pack()

winner_label = Label(window, text="Let's start the game!", font=font.Font(size=13), fg="green", pady=8)
winner_label.pack()

input_frame = Frame(window)
input_frame.pack()

player_options = Label(input_frame, text="Your Options", font=app_font, fg='grey')
player_options.grid(row=0, column=0, pady=8)