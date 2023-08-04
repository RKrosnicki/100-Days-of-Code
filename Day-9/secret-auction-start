go_on = True
bids_dict = {}

while go_on:
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    done = input("Is there anyone else willing to bid? (yes/no) ").lower()
    bids_dict[name] = bid

    if done == "yes":
        go_on = True
    elif done == "no":
        go_on = False
    else:
        check = 1
        while check == 1:
            done = input("Try again \nIs there anyone else? (yes/no) ")
            if done == "yes" or done == "no":
                check = 0
            if done == "yes":
                go_on = True
            elif done == "no":
                go_on = False
    clear()

highest_bid = 0
for bidder in bids_dict:
    if bids_dict[bidder] > highest_bid:
        winner = bidder
        highest_bid = bids_dict[bidder]

print(logo)
print(f"{winner} is a winner with a bid of {highest_bid}")
