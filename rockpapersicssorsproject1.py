import random

print("0 = Rock")
print("1 = Paper")
print("2 = Scissors")

user = int(input("Enter your choice (0/1/2): "))
computer = random.randint(0, 2)

print("Computer choice:", computer)

if user == computer:
    print("Match Draw")

elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You Win")

elif user in [0, 1, 2]:
    print("Computer Wins")

else:
    print("Invalid Choice")