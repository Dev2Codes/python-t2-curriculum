# extern
import re
    
# Problem 1
# Ask the user for a sentence.
# Print how many words it has.
# (Hint: split the sentence by spaces)

sentence:str = input("Enter a sentence (not over 2 years, got it!): ")
words:list[str] = sentence.split(" ")
print("Number of words in sentence:", len(words))

# or

sentencee:str = input("ENCHANCED VERSION (now smarter): Enter a sentence (not over 2 years, got it!): ")
wordse:list[str] = re.split(r"[\s+;:?!,./]", sentencee)
print("Number of words in sentence:", len(wordse))

# Problem 2
# Ask the user for a word.
# Build a new string that turns every vowel into "*".
# Example: "hello" -> "h*ll*"

word:str = input("Enter a word: ")
nword:str = str()
vowels:str = "aeiou"

for char in word:
    if char.lower() in vowels:
        nword += "*"
        continue
    nword+=char
print("New word:" + nword)


# Problem 3
# Ask the user for a word.
# Print the first index where the letter "a" appears.
# If there is no "a", print -1.

word:str = input("Enter a word (again!!!): ")
found:bool = False

for char in word:
    if char == "a":
        print("Found object \"a\" at index:", word.index(char))
        found = True
        break

if not found:
    print("-1")

# or

wordee:str = input("ENCHANCED VERSION (now simpler): Enter a word (again!!!): ")
print("Index of first 'a':", wordee.find("a"))

# Problem 4
# Ask the user for two words.
# Print the longer word. If they are the same length, print "Tie".
word1:str = input("Enter the first word: ")
word2:str = input("Enter the second word: ")

if len(word1) > len(word2):
    print("Longer word is:", word1)
elif len(word2) > len(word1):
    print("Longer word is:", word2)
else:
    print("it's a tie!")


# Problem 5
# Ask the user for a phrase.
# Build a new string that keeps only letters (remove spaces and punctuation).
# For this problem, remove commas and periods too.

phrase:str = input("Enter a phrase: ")
npharse:str = str()
for char in phrase:
    if char.isalpha():
        npharse += char

print("New phrase:", npharse)
