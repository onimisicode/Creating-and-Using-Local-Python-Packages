import random

player_wins = 0
CPU_wins = 0


options = ["R", "P", "S"]

while True:
    print("Welcome To Rock_Paper_Scissors Game")
    print("Note: ")
    print('"R" for "Rock"')
    print('"P" for "Paper"')
    print('"S" for "Scissors"')

    player = input("Player (Pick R/P/S or Input Q to quit): ")
    if player == "q":
        break 
    if player not in options:
        print("Invalid Input! Input R,P or S")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper:1, scissors: 2
    CPU_pick = options[random_number]
    print("Computer picked", CPU_pick + "-")

    if player == "R" and CPU_pick == "S":
        print("Congratulation You Win!")
        break

    elif player == "S" and CPU_pick == "P":
        print("Congratulation You Win!")
        break

    elif player == "P" and CPU_pick == "R":
        print("Congratulation You Win!")
        break

    elif player == "R" and CPU_pick == "R":
        print("It's A Tie! Play Again!")
        continue

    elif player == "P" and CPU_pick == "P":
        print(" It's A Tie! Play Again!")
        continue

    elif player == "S" and CPU_pick == "S":
        print(" It's A Tie! Play Again!")
        continue
    
    else:
        print("You lose!")
        break


print("Goodbye")

