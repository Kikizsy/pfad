import random

print("Welcome to the Rock, Paper, Scissors game!")

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() != 'yes':
        break
