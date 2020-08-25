# Write your code here

human_play = input().lower()

if human_play == "rock":
    print("Sorry, but the computer chose paper")
elif human_play == "scissors":
    print("Sorry, but the computer chose rock")
elif human_play == "paper":
    print("Sorry, but the computer chose scissors")
else:
    print("Please choose a valid option")
