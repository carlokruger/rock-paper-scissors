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
