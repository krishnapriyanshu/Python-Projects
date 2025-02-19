import random
computer = random.choice([1, 0, -1])
youstr = input("Enter you choice: ")
youdict = {"s": 1, "w": 0, "g": -1}
reversedict = {1: "snake", 0: "water", -1: "gun"}

you = youdict[youstr]

print(f"you chose{reversedict[you]}\ncomputer chose{reversedict[computer]} ")

if(computer == you):
    print("it's a draw")
else:
    if(computer == 1 and you == -1):
        print("you win!")
    elif(computer == 1 and you == 0):
        print("computer wins!")
    elif(computer == 0 and you == 1):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("computer win!")
    elif(computer == -1 and you == 1):
        print("computer win!")
    elif(computer == -1 and you == 0):
        print("you win!")
    elif(computer == -1 and you == 1):
        print("computer win!")
    else:
        print("something went wrong")