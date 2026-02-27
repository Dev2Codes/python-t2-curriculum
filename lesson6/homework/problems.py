# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
score:tuple[int] = (98, 87, 81, 100)
avg:int = sum(score) / len(score)
print(avg)


# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
students:list[tuple[str, int]] = [("Ava", 95), ("Ben", 88), ("Kai", 73)]
hscore:int = 0
hstudent:str = ""

for student in students:
    if student[1] > hscore:
        hscore = student[1]
        hstudent = student[0]

print("{} recieved the high score of {}".format(hstudent, hscore))


# Problem 3
# Ask the user for a sentence.
# Split it into words.
# Create a list of tuples where each tuple is (word, length_of_word).
# Print the list.
sentence:str = input("Enter a sentence: ")
words:list[str] = sentence.split()
statistics:list[tuple[str, int]] = list()

for word in words:
    statistics.append((word, len(word)))

print(statistics)

# Problem 4
# Create a function called first_and_last(word).
# It should return a tuple containing the first and last letter of the word.
# Test it.

def first_and_last(word:str) -> tuple[str, str]:
    return (word[0], word[-1])

print(first_and_last("67"))
print(first_and_last("hello"))


# Problem 5
# Tuples can be dictionary keys.
# Create a dictionary where the keys are points like (x, y) and the values are colors.
# Add at least 3 points and print the dictionary.

coolers:dict[tuple[int, int], str] = {
    (1, 1): "Red",
    (2, 3): "Green",
    (4, 5): "Blue"
}

print(coolers)
