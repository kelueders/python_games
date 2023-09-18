import random

# The computer chooses a number and the user guesses the number with hints from the computer.
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Wrong, guess again. Too low.")
        elif guess > random_number:
            print("Wrong, guess again. Too high.")

    
    print(f"Great work, you guessed right. The number is {random_number}!")

# guess(10)

# The computer guesses a number that the user chooses, giving hints to the computer
def computer_guess(x):
    low = 1
    high = x
    go = '2'
    feedback = ''

    print("")
    print(f"Think of a number in your head between 1 and {x}. The computer will try to guess.")

    while go.isalpha() == False:
        go = input("Are you ready? Enter any letter to start: ")
        if go.isalpha() == False:
            print("Take your time and think of a number")
        continue

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high since high = low
        print(f"The computer guessed: {guess}")

        feedback = input(f"Is {guess} too high, low, or correct? 'h' = high   'l' = low    'c' = correct ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"The computer figured out your number is {guess}!")
        else:
            print(f"Please enter a valid letter.")

computer_guess(100)
        
    

    
            

