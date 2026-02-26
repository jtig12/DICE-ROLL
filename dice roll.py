import random


# define a function for roll
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    answer = input("Roll the dice? (y/n): ")
    if answer.isalpha():
        if answer.lower() == "y":
            x = roll()
            y = roll()
            print(f'{x}, {y}')
            if x == 1 and y == 1:
                print("You Failed!")
                break

        elif answer.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("invalid Choice")
    else:
        print(f"This shoul be either y or n")
