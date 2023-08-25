import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    a_word = input("Give me a word: ").upper()
    try:
        result = [data_dict[letter] for letter in a_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
