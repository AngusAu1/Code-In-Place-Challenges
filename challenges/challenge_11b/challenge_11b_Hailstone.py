"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    
    # What is the remainder when my_num is divided by 2?
    # If the remainder is 1, then the number was odd.

    # defined an input "my_num"
    # can calc the remainder by my_num % 2
    my_num = int(input("Enter a number:"))
    remainder = my_num % 2

    # When my_num = 1, the calculation will be end, thus I set 
    # the condition of the while loop as "my_num != 1"

    # if remainder == 1, then it is odd and calc the 3n+1
    # if remainder == 0, then it is even and calc n/2
    # and then update the remainder with then new my_num, and go into
    # the while loop again until it become 1.

    while my_num != 1:
        if remainder == 1:
            n = (3 * my_num) + 1
            print(f"{my_num} is odd, so I make 3n+1: {n}")
            my_num = n
            remainder = my_num % 2
        elif remainder ==0:
            n = my_num//2
            print(f"{my_num} is even, so I take half: {n}")
            my_num = n
            remainder = my_num % 2



if __name__ == "__main__":
    main()