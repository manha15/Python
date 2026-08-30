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

def player_choice(player_input):
    global player_score
    global computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)

    player_choice_label.config(text=" Your Selected: " + player_input[0])
    computer_choice_label.config(text=" Computer Selected: " + computer_input[0])   

    if player_input == computer_input:
        tie()

    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()

        elif(computer_input[1] == 2):
                #this means the player wins
                player_wins()

    elif(player_input[1] == 1):
            if(computer_input[1] == 0):
                computer_wins()

            elif(computer_input[1] == 2):
                player_wins()
    elif(player_input[1] == 2):
                if(computer_input[1] == 0):
                    computer_wins()
    
                elif(computer_input[1] == 1):
                    player_wins()


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

rock_btn = Button(input_frame, text="Rock", bg="silver", padx=5, bd=0, width=15, command=lambda:player_choice(options[0]))
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text="Paper", bg="silver", padx=5, bd=0, width=15, command=lambda:player_choice(options[1]))
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text="Scissor", bg="silver", padx=5, bd=0, width=15, command=lambda:player_choice(options[2]))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

score_label = Label(input_frame, text="Score: ", font= app_font, fg="grey")
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text="You selected: ", font=app_font)
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text="Your score: ", font= app_font, fg="grey")
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text="Computer selected: ", font=app_font, fg="black")
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text="computer score: ", font= app_font, fg="black")
computer_score_label.grid(row=4, column=2, pady=5, padx=(10,0))

window.geometry('700x300')
window.mainloop()