# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
n:int = int(input("Gimme an integer: "))

for i in range(0, n+1, 3):
    print(i)


# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
n = int(input("Gimme another integer: "))

for i in range(1, n+1):
    print("{}^2 = {}".format(i, i**2))



# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).

n = int(input("Gimme one more integer: "))

for i in range(n, -1, -1):
    print("{}...".format(i))
print("Blast off!")


# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"

word:str = input("Gimme a word: ")
nword:str = str()

for i in range(5):
    nword += word+" "

nword = nword.rstrip()

print(nword)

# or

wordle:str = input("(ENCHANCED: NOW SIMPLER) gimme a word: ")
nwordle:str = (wordle + " ") * 5
nwordle = nwordle.rstrip()
print(nwordle)

# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.

n = int(input("Gimme an integer (AGAIN!!): "))
iter:list[int] = range(1, n+1, 2)

print("There are {} even numbers from 1 to {}".format(len(iter), n))

#or

n = int(input("Gimme an integer (AGAIN!! AGAIN!!): "))
print("There are {} even numbers from 1 to {}".format(n//2, n))
