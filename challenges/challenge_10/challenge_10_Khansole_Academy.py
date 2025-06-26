import random

def main():
    print("Khansole Academy")

    # x and y is defined as two numbers that for the addition problem
    # random.randint(10, 100) is control the number as 2-digit integers (10 through 99)

    x = random.randint(10, 100)
    y = random.randint(10, 100)

    # defined ans as the result of the addition problem x + y
    # using int() to ensure the addition as integer
    ans = int(x + y)

    # print the random gen numbers x & y
    # z is defined that the user input answer
    print("What is " + str(x) + " + " + str(y) + "?")
    z = int(input("Your answer: "))
        
    # using if-else to check the ans is correct or not
    if ans == z:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is " + str(ans))

    
    
if __name__ == '__main__':
    main()