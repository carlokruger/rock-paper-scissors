# Rock Paper Scissors (Lizard Spock)

## Stage 1: Unfair computer
### Description
Rock, paper, scissors is a well-known hand game. Each one of two players simultaneously forms one of three shapes with their hands, and then, depending on the chosen shapes, the winner is determined: rock beats scissors, paper wins over rock, scissors beat paper.
The game is widely used to make a fair decision between equal options.

So, let's start with an unfair version! :)

Write a program that reads input specifying which option the user has chosen. Then your program should make the user lose! That is, your program should always choose an option that defeats the one picked by the user. After finding this option, output a line Sorry, but the computer chose <option>, where <option> is the name of option that the program picked depending on the user's input.
For example, if the user enters rock, the program should print Sorry, but the computer chose paper and so on.

Please, pay attention to the format of the output. It should be exactly the same as in the example, including capital letters and punctuation. No additional strings should be printed!

### Objectives
Your program should:

1. Take an input from the user
2. Find an option that wins over the user's option
3. Output a line: Sorry, but the computer chose <option>


## Stage 2: Equalizing chances
### Description
Well, now let's do something real. Nobody wants the game where you always lose.
Using the power of the random module, we'll make a truly interesting game.

You should write a program that reads input from the user, chooses a random option and then says who won, the user or the computer.
There are a few examples below, providing output for any outcome (<option> is the option chosen by your program):

Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed

### Objectives
Your program should:

1. Read user's input specifying the option that user has chosen
2. Choose a random option
3. Compare the options and determine the winner
4. Output a line depending on the result of the game:
  * Lose -> Sorry, but the computer chose <option>
  * Draw -> There is a draw (<option>)
  * Win -> Well done. The computer chose <option> and failed

## Stage 3: Endless game
### Description
Wasn't that pretty cool?

But the game is really short so far: nobody plays just a single shot of rock-paper-scissors. We need to do some literally unstoppable game for unstoppable players. Not literally unstoppable, of course: let's implement a way to stop your program.

Improve your program so it would take an unlimited number of inputs until the user enters !exit. After entering !exit the program should print Bye! and terminate. Also, let's try to handle invalid inputs: your program should be ready that there may be a typo in user's input, or that a user may just enter complete gibberish instead of a normal command. So, in case the input doesn't correspond to any known command (option name or !exit), your program should output the line Invalid input

### Objectives
Your program should:

1. Take an input from the user
2. If the input is !exit, output Bye! and stop the game
3. If the input is the name of the option, then:
4. Pick a random option
5. Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
  * Lose -> Sorry, but the computer chose <option>
  * Draw -> There is a draw (<option>)
  * Win -> Well done. The computer chose <option> and failed
6. If the input corresponds to anything else, output Invalid input
7. Do it all over again

## Stage 4: Scoring the game
### Description
People love to see their results as they're running to their goal.
So, let's learn how to show the user the score of the game.

When the game starts, the user should enter his/her name. After that, the program should greet the user and read a file namedrating.txt . This is a file containing current scores for different players. You can see the file format below: it's just lines containing user's name and his/her score divided by a single space.

Tim 350
Jane 200
Alex 400
If there’s a record for the user with the same name in the file, the program should take his/her rating and use it as a reference point for counting current user’s score (for example, if the user entered name Tim, then his score at the start of the game will be 350). If the user's name isn't written in the file, then your program should count user's score from 0.

You don't need to write anything in the rating.txt file!

The program should print user's score when the user enters !rating. For example, if your rating is 0 then the program should print:

Your rating: 0
Your program should add 50 points to the player for every draw, 100 for every win, and nothing for losing.

### Objectives
Your program should:

1. Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
2. Read input specifying the user's name and output a new line Hello, <name>
3. Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
4. Play the game by the rules defined on the previous stages:
5. Read user's input
6. If the input is !exit, output Bye! and stop the game
7. If the input is the name of the option, then:
8. Pick a random option
9. Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
  * Lose -> Sorry, but the computer chose <option>
  * Draw -> There is a draw (<option>)
  * Win -> Well done. The computer chose <option> and failed
10. For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
11. If the input corresponds to anything else, output Invalid input
12. Play the game again