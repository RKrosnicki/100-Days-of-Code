import random

def higher_lower(winner):
    A = winner
    global score
    if score > 0:
        print(f"You're right, {winner['name']} is on top!\nCurrent score: {score}\n")
    B = random.choice(data)
    data.remove(B)
    return A, B


def check_answer(followers_a, followers_b):
    if followers_a > followers_b:
        return attempt == "a"
    elif followers_b > followers_a:
        return attempt == "b"


score = 0

winner = random.choice(data)
data.remove(winner)

A, B = higher_lower(winner)
alive = True

while alive:

    clear() #comment it if you're on PyCharm
    print(logo)
    A, B = higher_lower(winner)
    print(f'A is {A["name"]}, a {A["description"]} from {A["country"]}')
    print(f"Hint A: {A['follower_count']}")

    print(vs)

    print(f'B is {B["name"]}, a {B["description"]} from {B["country"]}')
    print(f"Hint B: {B['follower_count']}")
    attempt = input("Which one is more popular on Instagram? ").lower()

    if attempt == "a":
        if A["follower_count"] > B["follower_count"]:
            winner = A
            score += 1
        else:
            print("You're wrong!")
            print(f"Your score is {score}")

            alive = False
    elif attempt == "b":
        if B["follower_count"] > A["follower_count"]:
            winner = B
            score += 1
        else:
            print("You're wrong!")
            alive = False
            print(f"Your score is {score}")
    else:
        print("I said A or B. /n Maybe you'll be smarter next time!")
        alive = False
