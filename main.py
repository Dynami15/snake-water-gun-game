import random
'''
1 for snake 
-1 for water 
0 for gun
'''
#using ramdom library i am generating random number from computer (0,1,-1)

computer = random.choice([-1, 1 , 0])

#taking user input

youstr = input("Enter your choice:")

#using dictionary if user press s or g or w then it convert into 1 or 0 or -1

youDict = {"s":1, "w":-1, "g":0}

#using reverse dictionary we can print the input taken by computer and user

reverseDict={1:"Snake", -1:"Water", 0:"Gun"}

#storing usser input in a variable

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

#possible cases of the game!!

if(computer == you):
    print("Draw!!")
else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You lose!")

    else:
        print("Oops! Something went wrong.")







