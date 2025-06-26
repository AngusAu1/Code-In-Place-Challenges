import random

def main():
    # input how many sides of the dice
    dice_sides = int(input("How many sides does your dice have? "))

    # x is the random int number would be return that based on the inputted dice sides 
    x = random.randint(1, dice_sides)

    # print the result
    print("Your roll is " + str(x))

if __name__ == '__main__':
    main()