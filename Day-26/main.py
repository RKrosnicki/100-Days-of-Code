import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

a_word = input("Give me a word: ")
a_word = a_word.upper()

result = [data_dict[letter] for letter in a_word]

print(result)
