def main():
    """
    You should write your code here. 
    """

    # define an input for user to input a current numer
    curr_value = int(input("Enter a number: "))

    # using while loop to double up the enter no
    # and it will be repeat to double up until the value is 100 or greater
    while curr_value <= 100:
        curr_value = curr_value * 2
        print(curr_value)
    

if __name__ == '__main__':
    main()