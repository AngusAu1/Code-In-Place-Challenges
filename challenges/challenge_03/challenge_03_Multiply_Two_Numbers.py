"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")

    # 1. Prompt the user to enter the first number.
    # 2. Read the input and convert it to an integer.
    first_no = int(input("Enter first number: "))

    # 3. Prompt the user to enter the second number.
    # 4. Read the input and convert it to an integer.
    second_no = int(input("Enter second number: "))

    # 5. Calculate the value of multiplying the two numbers.
    multiple_ans = first_no * second_no

    # 6. Print the value
    print(multiple_ans)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()