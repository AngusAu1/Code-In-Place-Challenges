def main():
    """
    You should write your code here. 
    """
    # print("The Ancient Game of Nimm")  # Delete this line and write your code here! :)

    # x is the starting number of stones
    # defined the constant as 20
    x = 20

    # using the while loop for looping the game that started from x = 20
    # when condition x >=1 is ture, then keep it looping
    while x >= 1:
        
        print("There are " + str(x) + " stones left.")
        y = int(input("Player 1 would you like to remove 1 or 2 stones?"))

        # using the while loop to check user input is 1 or 2, if not, then ask user to input it again
        while y > 2 or y < 1:
            y = int(input("Please enter 1 or 2: "))
        x = x - y
        
        # entry row
        print()
        
        # check when the final result is smaller than 0, then game over and break the while loop
        # if the result is 0, then announce the winner as Player 2
        if x < 0:
            print("Game over")
            break
        elif x == 0:
            print("Player 2 wins!")
            break

        print("There are " + str(x) + " stones left.")
        y = int(input("Player 2 would you like to remove 1 or 2 stones?"))

        # using the while loop to check user input is 1 or 2, if not, then ask user to input it again
        while y > 2 or y < 1:
            y = int(input("Please enter 1 or 2: "))
        x = x - y

        # entry row
        print()

        # check when the final result is smaller than 0, then game over and break the while loop
        # if the result is 0, then announce the winner as Player 1
        if x < 0:
            print("Game over")
            break
        elif x == 0:
            print("Player 1 wins!")
            break


if __name__ == '__main__':
    main()