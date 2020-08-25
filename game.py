import random
# Write your code here

choices = ["rock", "paper", "scissors"]

human_play = input().lower()
ai_play = random.choice(choices)

if human_play == "rock":
    if ai_play == "rock":
        print("There is a draw {}".format(ai_play))
    elif ai_play == "paper":
        print("Sorry, but the computer chose {}".format(ai_play))
    elif ai_play == "scissors":
        print("Well done. The computer chose {} and failed".format(ai_play))

elif human_play == "scissors":
    if ai_play == "rock":
        print("Sorry, but the computer chose {}".format(ai_play))
    elif ai_play == "paper":
        print("Well done. The computer chose {} and failed".format(ai_play))
    elif ai_play == "scissors":
        print("There is a draw {}".format(ai_play))

elif human_play == "paper":
    if ai_play == "rock":
        print("Well done. The computer chose {} and failed".format(ai_play))
    elif ai_play == "paper":
        print("There is a draw {}".format(ai_play))
    elif ai_play == "scissors":
        print("Sorry, but the computer chose {}".format(ai_play))

else:
    print("Please choose a valid option")
