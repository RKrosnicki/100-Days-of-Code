from random import randrange

wanna_play = input("Wanna play? (y/n) ")

while wanna_play == "y":
    clear() #comment it if you're on PyCharm

    def choose_difficulty():
        """Asks for difficulty, and returns number of lives."""

        difficulty = input("Choose difficulty. \nWanna play it easy or play hard? (easy/hard) ").lower()

        if difficulty == "easy":
            print(f"You choose {difficulty}")
            return 10
        elif difficulty == "hard":
            print(f"You choose {difficulty}")
            return 5
        else:
            print("I've asked nicely. Now look what you've done.")
            return 3

    def check(number):
        """Compares players guess with the answer, and lowering lives if needed."""

        global answer
        global done
        global lives
        if number == answer:
            done = True
            return print(f"You guessed it! Answer is {answer}! ")
        elif number > answer:
            done = False
            lives -= 1
            return print("Too high!")
        else:
            done = False
            lives -= 1
            return print("Too low!")

    done = False

    print(logo)

    print("Welcome to Guess The Number game!")

    lives = choose_difficulty()

    answer = randrange(100)
    print("I'm thinking of a number between 1 and 100")

    while lives > 0:
        print(f"You've got {lives} lives left.")
        guess = int(input("\nGuess the Number! "))
        check(guess)

        if done == True:
            break
    else:
        print(f"You're out of lives. Answer was {answer}!\nYou lost!")

    wanna_play = input("\nDo you want another run? (y/n) ")
else:
    if wanna_play == "n":
        print(f"\nGoodbye! \n{bye}")
    else:
        print("\nCould've just say no...")
