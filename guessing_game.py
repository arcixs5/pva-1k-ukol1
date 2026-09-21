import random
def level_one():
    random_number = random.randint(1, 100)
    print("Guess the number between 1 and 100")
    guess = input("")
    attempts = 1
    while random_number != guess:
        if ValueError:
            print("Invalid input")
            attempts += 1
            guess = input("")
        if int(guess) > 100:
            attempts += 1
            print("the maximum number is 100 mate")
            guess = input("")
        elif int(guess) < 1:
            attempts += 1
            print("the minimum number is 1 mate")
            guess = input("")
        elif random_number > int(guess):
            attempts += 1
            print("higher")
            guess = input("")
        elif random_number < int(guess):
            attempts += 1
            print("lower")
            guess = input("")
    if random_number == int(guess):
        print("Correct")
        print("number of attempts: " + str(attempts))
        print("if you want to play again type: Yes")
        play_again = input("")
        if play_again == "Yes":
            level_one()
        else:
            print("GG")

level_one()