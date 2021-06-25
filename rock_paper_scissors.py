from random import randint

userWins = 0
computerWins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:

    randomNumber = randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computerPick = options[randomNumber]

    userPick = input("\nType rock/paper/scissors or q to quit: ").lower()

    if userPick == "q":
        break
    elif userPick not in options:
        continue

    print("You picked", userPick, "and computer picked", computerPick, end=".")

    if userPick == "rock" and computerPick == "scissors":
        print("\nYou won!")
        userWins += 1
        print()

        user = input("Do you want to know the score right now?\n Press y/n: ").lower()

        if user == "y" or user == "yes":
            if userWins > computerWins:
                print("\nThe score right now is:", userWins, "-",computerWins, "to you so far.")
            elif computerWins > userWins:
                print("\nThe score right now is:", computerWins, "-",userWins, "to me so far.")
            else:
                print("\nThe score right now is a tie, it's:", userWins, "-",computerWins, "so far!!!")

    elif userPick == "paper" and computerPick == "rock":
        print("\nYou won!")
        userWins += 1
        print()

        user = input("Do you want to know the score right now?\n Press y/n: ").lower()

        if user == "y" or user == "yes":
            if userWins > computerWins:
                print("\nThe score right now is:", userWins, "-",computerWins, "to you so far.")
            elif computerWins > userWins:
                print("\nThe score right now is:", computerWins, "-",userWins, "to me so far.")
            else:
                print("\nThe score right now is a tie, it's:", userWins, "-",computerWins, "so far!!!")

    elif userPick == "scissors" and computerPick == "paper":
        print("\nYou won!")
        userWins += 1
        print()

        user = input("\nDo you want to know the score right now?\n Press y/n: ").lower()

        if user == "y" or user == "yes":
            if userWins > computerWins:
                print("\nThe score right now is:", userWins, "-",computerWins, "to you so far.")
            elif computerWins > userWins:
                print("\nThe score right now is:", computerWins, "-",userWins, "to me so far.")
            else:
                print("\nThe score right now is a tie, it's:", userWins, "-",computerWins, "so far!!!")

    elif userPick == computerPick:
        print("\nWe tied!!!")
        ties += 1
        print()

        user = input("Do you want to know the score right now?\n Press y/n: ").lower()

        if user == "y" or user == "yes":
            if userWins > computerWins:
                print("\nThe score right now is:", userWins, "-",computerWins, "to you so far.")
            elif computerWins > userWins:
                print("\nThe score right now is:", computerWins, "-",userWins, "to me so far.")
            else:
                print("\nThe score right now is a tie, it's:", userWins, "-",computerWins, "so far!!!")

    else:
        print("\nYou lost!")
        computerWins += 1
        print()

        user = input("Do you want to know the score right now?\n Press y/n: ").lower()

        if user == "y" or user == "yes":
            if userWins > computerWins:
                print("\nThe score right now is:", userWins, "-",computerWins, "to you so far.")
            elif computerWins > userWins:
                print("\nThe score right now is:", computerWins, "-",userWins, "to me so far.")
            else:
                print("\nThe score right now is a tie, it's:", userWins, "-",computerWins, "so far!!!")

print()
print("You won", userWins, "times.")
print("The computer won", computerWins, "times.")
print("We drew:", ties, "times!!!", end=" (very lucky indeed)")
print("Goodbye!")
