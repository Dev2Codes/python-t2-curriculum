# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
word:str = input("enter a word: ")

print(word[::-1])


# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
wrd = input("enter a word (again!): ").lower()
lttr = input("enter a letter: ").lower()

print("Founded {} instances of \"{}\" in the word".format(wrd.count(lttr), lttr))



# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com").
email:str = input("please enter your email: ")

domain:str = email[email.find("@")+1:]

print("Found domain: {}".format(domain))


# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
wordle:str = input("enter a word (again! UGH!): ")

nwordle:str = wordle[1:][:-1]

if nwordle == "":
    print("String too short, just a blank line now!")
else:
    print(nworlde)


# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short".

sentence:str = input("enter a sentence (not over 20 years! >:( ): ")

if (len(sentence) > 20):
    print("Long!")
else:
    print("Short!")
