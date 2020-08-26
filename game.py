import random
# Write your code here

default = ["rock", "paper", "scissors"]
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

text = input("Input game:")  # rock,paper,scissors,lizard,spock
print("Okay, let's start")

if len(text) == 0:
    game = default
else:
    game = text.split(",")

num_winners = (len(game) - 1) / 2  # 2
winners = []

if player in ratings:
    current_score = ratings[player]

while True:
    human_play = input("Input choice:").lower()  # scissors
    ai_play = random.choice(game)  # spock

    if human_play == "!rating":
        print("Your rating: ", current_score)

    elif human_play == "!exit":
        print("Bye!")
        break

    elif human_play not in game:
        print("Invalid input")

    if human_play in game:
        mid_point = game.index(human_play)  # 3

        if mid_point > num_winners:  # True
            winners = game[mid_point + 1:]
            winners.extend(game[:int(mid_point - num_winners)])

        elif mid_point < num_winners:
            winners = game[mid_point + 1: int(mid_point + num_winners) + 1]

        elif mid_point == num_winners:
            winners = game[mid_point + 1:]

        if human_play == ai_play:
            print("There is a draw ({})".format(ai_play))
            current_score += 50

        elif ai_play in winners:
            print("Sorry, but the computer chose {}".format(ai_play))

        elif ai_play not in winners:
            print("Well done. The computer chose {} and failed".format(ai_play))
            current_score += 100


