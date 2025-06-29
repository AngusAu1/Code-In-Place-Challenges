import random

# defined the constant numbers
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """

    # Using for loop to print the random no. which the range in 1 to 100, and loop it in 10 rounds.
    for i in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value)
        

if __name__ == '__main__':
    main()