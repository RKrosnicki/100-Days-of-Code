PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in names_list:
    stripped_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as f:
        f.writelines(letter.replace(PLACEHOLDER, stripped_name))
