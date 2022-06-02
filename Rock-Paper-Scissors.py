import random

# WINNING PATTERNS
# Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,
# Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
# Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock,
# Rock crushes Scissors

win = [("scissors","paper"), ("paper","rock"), ("rock","lizard"),
       ("lizard","Spock"), ("Spock","scissors"), ("scissors","lizard"),
       ("lizard","paper"), ("paper","Spock"), ("Spock","rock"),
       ("rock","scissors")]

# INSTRUCTIONS
print("There are 6 rounds.\nYou are playing against Computer.\nYou will win if you have a higher point.\nEnter scissors, paper, rock, lizard or Spock.")

# CHOICES FOR THE COMPUTER TO CHOOSE FROM
choices = ["scissors", "paper", "rock", "lizard", "Spock"]

# TO COUNT THE NUMBER OF ROUNDS
count = 0
# TO COUNT THE PLAYER'S POINTS
playerPoints = 0
# TO COUNT THE COMPUTERS' POINTS
computerPoints = 0

# WHILE LOOP TO SET THE NUMBER OF ROUNDS
while count != 6:
    # INPUT FOR PLAYER'S CHOICE
    player = input("What is your move? ")
    # COMPUTER RANDOMLY SELECT CHOICE FROM CHOICES LIST
    computer = random.choice(choices)
    # UNCOMMENT THE LINE BELOW IF YOU WISH TO SEE COMPUTERS' CHOICE
    #print(computer)

    # DIFFERENT CHOICES
    if player != computer:
        # CHECK FOR PATTERNS
        playerWins = (player,computer)
        computerWins = (computer,player)
        if playerWins in win:
            if playerWins == win[0]:
                #print("✂ cuts 📃 \nYou Won!")
                print("Scissors cuts paper \nYou Won!")
            elif playerWins == win[1]:
                print("Paper covers rock \nYou Won!")
            elif playerWins == win[2]:
                print("Rock crushes lizard \nYou Won!")
            elif playerWins == win[3]:
                print("Lizard poisons Spock \nYou Won!")
            elif playerWins == win[4]:
                print("Spock smashes scissors \nYou Won!")
            elif playerWins == win[5]:
                print("Scissors decapitates lizard \nYou Won!")
            elif playerWins == win[6]:
                print("Lizard eats paper \nYou Won!")
            elif playerWins == win[7]:
                print("Paper disproves Spock \nYou Won!")
            elif playerWins == win[8]:
                print("Spock vapourizes rock \nYou Won!")
            elif playerWins == win[9]:
                print("Rock crushes scissors \nYou Won!")
            playerPoints += 1
        elif computerWins in win:
            if computerWins == win[0]:
                print("Scissors cuts paper \nComputer Wins!")
            elif computerWins == win[1]:
                print("Paper covers rock \nComputer Wins!")
            elif computerWins == win[2]:
                print("Rock crushes lizard \nComputer Wins!")
            elif computerWins == win[3]:
                print("Lizard poisons Spock \nComputer Wins!")
            elif computerWins == win[4]:
                print("Spock smashes scissors \nComputer Wins!")
            elif computerWins == win[5]:
                print("Scissors decapitates lizard \nComputer Wins!")
            elif computerWins == win[6]:
                print("Lizard eats paper \nComputer Wins!")
            elif computerWins == win[7]:
                print("Paper disproves Spock \nComputer Wins!")
            elif computerWins == win[8]:
                print("Spock vapourizes rock \nComputer Wins!")
            elif computerWins == win[9]:
                print("Rock crushes scissors \nComputer Wins!")
            computerPoints += 1
        # PLAYER DID NOT INPUT scissors, paper, rock, lizard or Spock
        else:
            print("Invalid response \nComputer Wins!")
            computerPoints += 1

    # DRAW, SAME CHOICES
    elif player == computer:
        print("Draw, Player and Computer gets 1 point")
        playerPoints += 1
        computerPoints += 1

    # EMPTY LINE FOR A NEATER/CLEARER VIEW
    print("")

    # INCREMENT TO CONTROL THE NUMBER OR ROUNDS
    count += 1

# COMPARISON TO DETERMINE WHO IS THE CHAMPION
if playerPoints > computerPoints:
    print("You are the champion! 🏆")
elif playerPoints == computerPoints:
    print("You are both champions!! 🏆🏆")
else:
    print("Computer is the champion, Try Again! 💻")