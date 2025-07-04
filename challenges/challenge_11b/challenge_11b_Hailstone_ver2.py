"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""


def main():
    my_num = int(input("Enter a number: "))

    while my_num != 1:
        if my_num % 2 == 0:
            next_num = my_num // 2
            print(f"{my_num} is even, so I take half: {next_num}")
        else:
            next_num = 3 * my_num + 1
            print(f"{my_num} is odd, so I make 3n + 1: {next_num}")
        my_num = next_num



if __name__ == "__main__":
    main()