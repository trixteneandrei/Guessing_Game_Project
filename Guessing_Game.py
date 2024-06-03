import random  # Importing the random module to generate random numbers
import time    # Importing the time module for adding delays

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)  # Adding a delay of 3 seconds for dramatic effect
print("Picking a number...")
time.sleep(2)  # Adding a delay of 2 seconds
guess = int(input("What is your guess?: "))  # Asking the user to input their guess
correct_number = random.randint(1, 100)  # Generating a random number between 1 and 100 as the correct answer
guess_count = 1  # Initializing the guess count to 1

while guess != correct_number:  # Looping until the user's guess matches the correct number
    time.sleep(1)  # Adding a delay of 1 second
    guess_count += 1  # Incrementing the guess count
    if guess < correct_number:  # If the guess is lower than the correct number
        guess = int(input("Wrong, you need to guess higher. What is your guess?: "))  # Asking for a higher guess
    else:  # If the guess is higher than the correct number
        guess = int(input("Wrong, you need to guess lower. What is your guess?: "))  # Asking for a lower guess

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")  # Printing the result