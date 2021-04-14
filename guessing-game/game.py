# Put your code here
# Pseudocode
# Display a greeting message to a player
print("Welcome to the Number Guessing Game!!!")
# Get playesr's name and guess and store it to the variables
user_name = input("What is your name? ")
user_tries = 1
number_to_guess = random.randint(1,100)
print (number_to_guess)
playing = True
while playing:
    user_guess = input("Guess number between 1 and 100 ")
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input. Please type a number...")
    else:
        print(f"Hello, {user_name}. You guess number is {user_guess}")
        if user_guess < 1 or user_guess > 100:
            print("Your number is out of scope. Please choose between 1 and 100.")
        elif user_guess > number_to_guess:
            print("Your guess is too high!")
            user_tries += 1
        elif user_guess < number_to_guess:
            print("Your guess is too low!")
            user_tries += 1
        elif user_guess == number_to_guess:
            print(f"Your guess {user_guess} is correct! It took you {user_tries} tries.")
            playing = False
            break
