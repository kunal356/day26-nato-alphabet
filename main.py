import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# #TODO 1. Create a dictionary in this format:
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)
word = input("Enter a word").upper()
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# {"A": "Alfa", "B": "Bravo"}
result = [data_dict[letter] for letter in word]

print(result)
