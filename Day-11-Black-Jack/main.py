import random
from logo import logo

def card_draw():
    card_pool = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    return random.choice(card_pool)

def wanna_play():
    play = input("Do you wanna play a game of Black Jack? (y/n) ")
    if play == "y":
        return True
    elif play == "n":
        return False
    else:
        print("You think you're funny? ")
        return False

def count_points(hand):
    score = 0
    for i in hand:
        if i == "J" or i == "Q" or i == "K":
            score += 10
        elif i == "A":
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += i
    return score

play = True

while play:
    #clear() # comment it if you're on PyCharm
    print(logo)
    go_on = True
    player_hand = [card_draw(), card_draw()]
    player_points = count_points(player_hand)
    computers_hand = [card_draw()]
    computers_score = count_points(computers_hand)

    print(f"Your hand is: {player_hand} and it gives you {player_points} points")
    print(f"Computer's hand is: {computers_hand} and it gives him {computers_score} points")

    hit = input("Hit or pass? (h/p) ")

    while hit == "h":
        player_hand.append(card_draw())
        player_points = count_points(player_hand)
        print(f"Your hand is: {player_hand} and it gives you {player_points} points")
        if player_points == 21:
            print("You win! ")
            go_on = False
            break
        elif player_points > 21:
            print("You loose! ")
            go_on = False
            break
        if go_on == True:
            hit = input("Hit or pass? (h/p) ")
        if hit == "p":
            break

    while computers_score < 17:
        computers_hand.append(card_draw())
        computers_score = count_points(computers_hand)
    if go_on == True and computers_score == 21:
        print(f"Computer's hand is {computers_hand} scoring {computers_score} points. \nYou loose! ")
    elif go_on == True and computers_score > 21:
        print(f"Computer's hand is {computers_hand} scoring {computers_score} points. \nYou win! ")
    elif go_on == True and player_points > computers_score:
        print(f"Computer's hand is {computers_hand} scoring {computers_score} points\nYou win!")
    elif go_on == True and player_points < computers_score:
        print(f"Computer wins with {computers_hand} in hand scoring {computers_score} points!")
    elif go_on == True and player_points == computers_score:
        print("It's a draw!")


    play = wanna_play()
else:
    print("Goodbye!")
