import random
# Write your code here

choices = ["rock", "paper", "scissors"]
current_score = 0

player = input("Enter your name:")
print("Hello,", player)

ratings = {}

file_open = open("rating.txt", "r")

for line in file_open:
    name, score = line.split()
    name = name.replace('\n', "")
    score = score.replace('\n', "")
    ratings.update({name: int(score)})

file_open.close()

if player in ratings:
    current_score = ratings[player]

while True:
    human_play = input().lower()
    ai_play = random.choice(choices)

    if human_play == "rock":
        if ai_play == "rock":
            print("There is a draw ({})".format(ai_play))
            current_score += 50
        elif ai_play == "paper":
            print("Sorry, but the computer chose {}".format(ai_play))
        elif ai_play == "scissors":
            print("Well done. The computer chose {} and failed".format(ai_play))
            current_score += 100

    elif human_play == "scissors":
        if ai_play == "rock":
            print("Sorry, but the computer chose {}".format(ai_play))
        elif ai_play == "paper":
            print("Well done. The computer chose {} and failed".format(ai_play))
            current_score += 100
        elif ai_play == "scissors":
            print("There is a draw ({})".format(ai_play))
            current_score += 50

    elif human_play == "paper":
        if ai_play == "rock":
            print("Well done. The computer chose {} and failed".format(ai_play))
            current_score += 100
        elif ai_play == "paper":
            print("There is a draw ({})".format(ai_play))
            current_score += 50
        elif ai_play == "scissors":
            print("Sorry, but the computer chose {}".format(ai_play))


    elif human_play == "!rating":
        print("Your rating: ", current_score)

    elif human_play == "!exit":
        print("Bye!")
        break

    else:
        print("Invalid input")
