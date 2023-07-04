import random

def play_game():
    # Initialize the score counters
    user_wins = 0
    computer_wins = 0
    draws = 0

    # Game loop
    while True:
        # Ask the user for their choice
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ")

        # Check if the user wants to quit
        if user_choice == "q":
            break

        # Validate the user's choice
        choices = ["rock", "paper", "scissors"]
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Generate the computer's choice randomly
        computer_choice = random.choice(choices)

        # Compare the choices and determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        # Display the current score
        print("Score: User -", user_wins, "| Computer -", computer_wins, "| Draws -", draws)

play_game()