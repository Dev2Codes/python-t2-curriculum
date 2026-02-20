# Problem 1
# Create a class called BankAccount.
# __init__ takes owner and balance.
# Make a method deposit(amount) that adds to balance.
# Make a method withdraw(amount) that subtracts only if there is enough money.
# Test it with a few deposits and withdrawals.

class BankAccount:
    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance
    
    def widthdraw(self, amount:float):
        if self.balance >= amount:
            self.balance-=amount
            print("{} withdrew ${}\nNew balance: ${}".format(self.owner, amount, self.balance))
        else:
            print("Not enough money to withdraw.")
    
    def deposit(self, amount:float):
        self.balance+=amount
        print("{} deposited ${}\nNew balance: ${}".format(self.owner, amount, self.balance))

bank:BankAccount = BankAccount("Bob", 100.0)
bank.deposit(67.0)
bank.widthdraw(41.0)
bank.widthdraw(89.0)

# Problem 2
# Create a class called Car.
# __init__ takes model and miles.
# Make a method drive(distance) that adds to miles.
# Create a Car and drive it a few times, printing miles each time.

class Car:
    def __init__(self, mode:str, miles:float):
        self.model = mode
        self.miles = miles
    
    def drive(self, distance:float):
        self.miles+=distance
        print("Your {} drove {} miles\nwith {} total miles".format(self.model, distance, self.miles))

mycar:Car = Car("Nissan Pathfinder 2025", 676767.0)
mycar.drive(100.0)
mycar.drive(50.0)

# Problem 3
# Create a class called ScoreKeeper.
# It stores a dictionary of player scores.
# Make a method add_points(name, points) that adds points for that player.
# Print the final dictionary after adding points for a few players.

class ScoreKeeper:
    def __init__(self):
        self.scores = {}

    def add_points(self, name:str, points:int):
        if name in self.scores:
            self.scores[name]+=points
            return 0
        self.scores[name] = points
    
    def print_scores(self):
        print("Scores:")
        for (name, score) in self.scores.items():
            print("{} : {}".format(name, score))

scorekeeper:ScoreKeeper = ScoreKeeper()
scorekeeper.add_points("Joe Mama", 10)
scorekeeper.add_points("Bob", 15)
scorekeeper.add_points("Joe Mama", 5)
scorekeeper.print_scores()

# Problem 4
# Create a class called Timer.
# It starts at 0 seconds.
# Make a method tick() that adds 1.
# Make a method reset() that sets it back to 0.
# Test tick() and reset().

class Timer:
    def __init__(self):
        self.seconds = 0
    
    def tick(self):
        self.seconds+=1
        print("ticked: {} seconds".format(self.seconds))
    
    def reset(self):
        self.seconds = 0
        print("reset: 0 seconds")

clocky:Timer = Timer()
clocky.tick()
clocky.tick()
clocky.reset()
clocky.tick()
clocky.tick()

# Problem 5
# Create a class called WordTracker.
# It stores a word (string).
# Make a method add_letter(letter) that adds the letter to the end.
# Make a method remove_last() that removes the last letter (if it exists).
# Test it.

class WordTracker:
    def __init__(self, word:str):
        self.word = word
    
    def add_letter(self, char:str):
        self.word+=char
        print("New string: {}".format(self.word))
    
    def remove_letter(self):
        if len(self.word) > 0:
            self.word = self.word[:-1]
            print("New string: {}".format(self.word))
        else:
            print("Tooo short!!")
