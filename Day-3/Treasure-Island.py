print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


answer = input("Where do you want to go? (left or right)\n").lower()

if answer != "left":
    print("Giant box just fell from the sky and crushed you. You died.\nGame over!")
else:
    answer = input("There's a lake ahead, and an island in the middle of it. What are you gonna do? (swim/wait)\n").lower()
    if answer == "swim":
        print("You apprently forgot you can't swim. You drowned.\nGame over!")
    else:
        print("You've just waited until lake is frozen, and you can now get to the island on foot.")
        answer = input("You can see three hatches: red, blue and yellow. Which are you gonna choose?\n").lower()
        if answer == "red":
            print("After entering red hatch, you tried to start a fire, to see better. Apparently there was some flamable gas in here. You're burnt to crisp.\nGame over!")
        elif answer == "blue":
            print("After opening blue hatch, some wild beasts got out. And eaten you.\nGame over!")
        elif answer == "yellow":
            print("After few minutes walk you enter a room with a chest in it. You open it, and nothing is trying to kill you.\nYou win!")
        else:
            print("Doing anything other than choosing a hatch means you've just surrendered your dream.\nYou lost!")
