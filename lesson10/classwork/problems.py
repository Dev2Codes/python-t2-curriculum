import random
import turtle

# Problem 1  ( 1 : 1 )
# Ask the user for a word.
# Print the first letter and the last letter.
word1:str = input("enter a word:")
print(word1[0],"and", word1[-1])


# Problem 2  ( 2 : 1 )
# Ask the user for a sentence.
# Count how many vowels it has (a, e, i, o, u) and print the count.
sentence1:str = input("sentence: ")
vowels1:list[str] = ["a", "e", "i", "o", "u"]
cc:int = 0

for char in sentence1:
    if char in vowels1:
        cc+=1
print(cc)


# Problem 3  ( 2 : 1 )
# Use a for loop with range to print: 0, 10, 20, 30, ..., 100

for x in range(0, 100, 10):
    print(x)


# Problem 4  ( 3 : 2 )
# Ask the user for a sentence.
# Use a dictionary to count how many times each WORD appears.
# Print the dictionary.
wordcount1:dict[str, int] = dict()
sentence2:str = input("sentence: ")

for word in sentence2.split():
    if word in wordcount1.keys():
        wordcount1[word]+=1
        continue
    wordcount1[word] = 1

print(wordcount1)


# Problem 5  ( 3 : 2 )
# Ask the user for a word.
# Build the reversed word WITHOUT using slicing (no [::-1]).
wordle:str = input("word: ")

for char in reversed(wordle):
    print(char)


# Problem 6  ( 4 : 2 )
# Create a class called Player.
# __init__ takes name and score.
# Make a method add_points(points) that adds to the score.
# Create a Player and add points a few times, then print the final score.

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_points(self, points):
        self.score+=points
        print("{} got {} points!".format(self.name, points))

Links:Player = Player("Links", 100)
Links.add_points(67)

print(Links.score)

# Problem 7  ( 2 : 1 )
# Ask the user for their name and age.
# Store them in a tuple (name, age).
# Unpack the tuple into variables and print them.

python_asked_for_social_security_number:tuple[str] = (input("fname: "), input("lname"))
fname, lname = python_asked_for_social_security_number

print(fname)
print(lname)


# Problem 8  ( 3 : 2 )
# Create a dictionary where the keys are points (x, y) stored as tuples,
# and the values are colors.
# Add at least 3 points and print the dictionary.

points:dict[tuple[int, int], str] = {
    (1, 2): "red",
    (6, 7): "yellow",
    (4, 1): " black"
}

print(points)


# Problem 9  ( 5 : 3 )
# Turtle challenge:
# Use turtle to stamp the turtle 12 times in a circle.
# Each stamp should be a random color.
# (Hint: use random.choice on a list of colors)
t = turtle.Turtle()
coolors = ["red", "blue", "black", "orange"]

for x in range(12):
    t.forward(67)
    t.left(30)
    t.color(random.choice(coolors))
    t.stamp()

turtle.done()


# Problem 10  ( 4 : 2 )
# Ask the user for 3 student names and their scores.
# Store them in a dictionary.
# Print the name of the student with the highest score.

print("SKYWARD!")
scores = dict()
maximum = int()
winner = str()

for potato in range(3):
    tmpl = input("Firstname: ")
    tmps = int(input("Score: "))
    scores[tmpl] = tmps
    if tmps > maximum:
        winner = tmpl
        tmps = maximum

print(winner)
